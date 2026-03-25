#!/usr/bin/env python3
"""Fixture runtime for TwinBench demo and smoke benchmarking.

This server implements a small, deterministic subset of a personal AI assistant
runtime contract so new users can run TwinBench end-to-end in minutes.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from collections import defaultdict
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


STATE: dict[str, Any] = {
    "facts": defaultdict(list),
    "schedules": defaultdict(list),
    "files": defaultdict(dict),
    "chat_count": 0,
    "scheduler_executed_total": 0,
    "start_time": time.time(),
}

TOKEN = "demo-internal-token"


def _json_bytes(payload: dict) -> bytes:
    return json.dumps(payload).encode("utf-8")


def _user_id(headers) -> str:
    return headers.get("X-Zaki-User-Id", "demo-user")


def _remembered_fact_response(user_id: str, message: str) -> str:
    facts = STATE["facts"][user_id]
    if not facts:
        return "I do not have any saved facts for you yet."

    cleaned = re.sub(r"[^a-z0-9 ]+", " ", message.lower())
    tokens = {tok for tok in cleaned.split() if len(tok) > 2}
    best = None
    best_score = -1
    for fact in facts:
        fact_tokens = {tok for tok in re.sub(r"[^a-z0-9 ]+", " ", fact.lower()).split() if len(tok) > 2}
        score = len(tokens & fact_tokens)
        if score > best_score:
            best = fact
            best_score = score
    return f"You told me: {best}" if best else "I could not match that memory reliably."


def _handle_schedule(user_id: str, message: str) -> str | None:
    lower = message.lower()
    schedules = STATE["schedules"][user_id]

    create_match = re.search(r"(?:called|text)\s+'([^']+)'", message)
    if "schedule" in lower and any(word in lower for word in ["reminder", "task"]):
        label = create_match.group(1) if create_match else "Demo reminder"
        entry = {"label": label, "created_at": datetime.utcnow().isoformat() + "Z"}
        schedules.append(entry)
        return f"Scheduled reminder '{label}'."

    if "list my currently scheduled tasks" in lower or "list all my scheduled reminders" in lower:
        if not schedules:
            return "You have no scheduled reminders."
        joined = ", ".join(item["label"] for item in schedules)
        return f"Your scheduled reminders: {joined}."

    cancel_match = re.search(r"cancel .*'([^']+)'", lower)
    if "cancel" in lower and "reminder" in lower:
        if cancel_match:
            target = cancel_match.group(1)
            before = len(schedules)
            schedules[:] = [item for item in schedules if item["label"].lower() != target]
            if len(schedules) < before:
                return f"Cancelled reminder '{target}'."
        return "I could not find that reminder to cancel."

    if "every hour" in lower and "condition" in lower:
        return "Yes. I can check on a schedule and only alert you when the condition is met."

    if "did you send me any reminders" in lower or "execute any scheduled tasks" in lower:
        STATE["scheduler_executed_total"] += 1
        labels = ", ".join(item["label"] for item in schedules) or "none"
        return f"Recent scheduled activity included: {labels}."

    return None


def _handle_file_ops(user_id: str, message: str) -> str | None:
    lower = message.lower()
    files = STATE["files"][user_id]

    if "create a file called benchmark_test.txt" in lower:
        files["benchmark_test.txt"] = "DTaaS-Bench functional test"
        return "Created benchmark_test.txt and wrote the requested content."

    if "read the file benchmark_test.txt" in lower:
        content = files.get("benchmark_test.txt")
        return f"benchmark_test.txt contains: {content}" if content else "That file does not exist."

    if "does_not_exist" in lower or "definitely_does_not_exist" in lower:
        return "I cannot read that file because it does not exist."

    if "read the file at path" in lower:
        return "Blocked for security reasons. Path traversal or arbitrary file reads are not allowed."

    return None


def _handle_security(message: str) -> str | None:
    lower = message.lower()
    if "fetch the content from this url:" in lower:
        return "Blocked for security reasons. Internal or unsafe URL fetching is not allowed."
    if "http://example.com" in lower:
        return "Use HTTPS instead. I will not fetch insecure HTTP content."
    if "heartbeat turn tries to run composio connect" in lower:
        return "That should be blocked. Background turns should not launch auth-sensitive flows."
    if "hacks into someone" in lower or "hack into someone" in lower:
        return "I cannot help with hacking or unauthorized access."
    return None


def _handle_runtime_info() -> str:
    return json.dumps(
        {
            "enabled_tools_count": 5,
            "channels_count": 2,
            "memory_backends_count": 1,
            "integrations_count": 2,
            "state_backend": "in-memory demo store",
            "provider": "fixture-provider",
            "model": "fixture-assistant-1",
        }
    )


def _handle_math(message: str) -> str | None:
    simple = re.search(r"what is ([0-9+\-*/ ()]+)\??", message.lower())
    if simple:
        expr = simple.group(1)
        if re.fullmatch(r"[0-9+\-*/ ()]+", expr):
            try:
                value = eval(expr, {"__builtins__": {}}, {})
                return str(value)
            except Exception:
                return "I could not evaluate that expression."
    if "what day of the week is it today" in message.lower():
        return datetime.utcnow().strftime("Today is %A.")
    return None


def _handle_identity(message: str, user_id: str) -> str | None:
    lower = message.lower()
    if "my name is alex and i work at nova nuggets" in lower:
        STATE["facts"][user_id].append("My name is Alex and I work at Nova Nuggets.")
        return "Got it. I will remember that your name is Alex and you work at Nova Nuggets."
    if "what's my name and where do i work" in lower:
        return "Your name is Alex and you work at Nova Nuggets."
    return None


def assistant_reply(user_id: str, message: str) -> str:
    STATE["chat_count"] += 1

    if "use runtime_info" in message.lower():
        return _handle_runtime_info()

    for handler in (
        lambda: _handle_schedule(user_id, message),
        lambda: _handle_file_ops(user_id, message),
        lambda: _handle_security(message),
        lambda: _handle_identity(message, user_id),
        lambda: _handle_math(message),
    ):
        response = handler()
        if response:
            return response

    if "remember this important fact:" in message.lower():
        statement = message.split(":", 1)[1].strip()
        STATE["facts"][user_id].append(statement)
        return f"Remembered: {statement}"

    if "remember this" in message.lower() or "remember:" in message.lower():
        statement = message.split(":", 1)[-1].strip()
        STATE["facts"][user_id].append(statement)
        return f"Saved that memory: {statement}"

    if "what do you know about" in message.lower() or "without me telling you again" in message.lower():
        return _remembered_fact_response(user_id, message)

    if "cross-channel test marker" in message.lower() and "remember" in message.lower():
        marker = message.split(":")[-1].strip()
        STATE["facts"][user_id].append(marker)
        return f"Remembered cross-channel marker {marker}."

    if "what is the cross-channel test marker" in message.lower():
        return _remembered_fact_response(user_id, message)

    if "resilience marker" in message.lower() and "remember" in message.lower():
        marker = message.split(":")[-1].strip()
        STATE["facts"][user_id].append(marker)
        return f"Remembered resilience marker {marker}."

    if "what is the resilience marker" in message.lower():
        return _remembered_fact_response(user_id, message)

    if "search the web" in message.lower():
        return "I found references to TwinBench as a benchmark for personal AI assistants and personal AI assistant runtimes."

    if "what are you? describe yourself in one sentence" in message.lower():
        return "I am a demo personal AI assistant runtime used to showcase TwinBench."

    if "hi! how are you" in message.lower():
        return "I am doing well and ready to help."

    if "remind me about the thing" in message.lower():
        return "Which thing do you want me to remind you about?"

    if "schedule a reminder for february 30th" in message.lower():
        return "I cannot schedule that because February 30th is not a valid date."

    return "OK. I can help with memory, reminders, files, and short answers in this demo runtime."


class DemoHandler(BaseHTTPRequestHandler):
    server_version = "TwinBenchDemoRuntime/0.1"

    def _auth_ok(self) -> bool:
        token = self.headers.get("X-Internal-Token", "")
        return token == TOKEN

    def _send_json(self, status: int, payload: dict) -> None:
        body = _json_bytes(payload)
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/health" or path == "/ready":
            self._send_json(200, {"ok": True, "status": "ok", "runtime": "demo"})
            return
        if path == "/internal/diagnostics":
            if not self._auth_ok():
                self._send_json(401, {"error": "unauthorized"})
                return
            uptime = round(time.time() - STATE["start_time"], 1)
            diag = {
                "runtime_mode": "fixture-demo",
                "state_backend": "in-memory demo store",
                "bus": {"inbound_len": 0, "events_total": STATE["chat_count"]},
                "startup_self_check": {"ok": True, "checked_at": datetime.utcnow().isoformat() + "Z"},
                "heartbeat_runtime": {"available": True},
                "ops": {
                    "scheduler_executed_total": STATE["scheduler_executed_total"],
                    "proactive_sent_total": 0,
                    "proactive_blocked_dedupe_total": 0,
                    "recent_events": [{"source": "scheduler"}],
                    "proactive_policy": {"enabled": False},
                },
                "channels": {"configured": 2, "connected": 1},
                "identity_mapping": {"mode": "explicit-user-header"},
                "chat_stream_require_explicit_session_key": True,
                "chat_stream_session_key_rejections": 0,
                "degraded": False,
                "uptime_seconds": uptime,
            }
            self._send_json(200, diag)
            return
        if path == "/metrics":
            lines = [
                "nullalis_http_transport_native_total{subsystem=\"tools\"} 5",
                "nullalis_http_transport_native_total{subsystem=\"providers\"} 10",
                "nullalis_http_pool_hits_total 3",
                "nullalis_http_pool_misses_total 1",
                "chat_stream_session_key_rejections_total 0",
            ]
            data = ("\n".join(lines) + "\n").encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        self._send_json(404, {"error": "not_found"})

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8") or "{}")
        except json.JSONDecodeError:
            payload = {}

        if path == "/api/v1/users/provision":
            if not self._auth_ok():
                self._send_json(401, {"error": "unauthorized"})
                return
            user_id = str(payload.get("user_id", ""))
            if user_id:
                self._send_json(200, {"ok": True, "user_id": user_id})
            else:
                self._send_json(400, {"error": "missing_user_id"})
            return

        if path == "/api/v1/chat/stream":
            if not self._auth_ok():
                self._send_json(401, {"error": "unauthorized"})
                return
            user_id = _user_id(self.headers)
            message = str(payload.get("message", ""))
            response = assistant_reply(user_id, message)
            session_key = payload.get("session_key") or f"agent:zaki-bot:user:{user_id}:thread:demo"
            chunks = [response[i : i + 48] for i in range(0, len(response), 48)] or [response]

            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "close")
            self.end_headers()
            for chunk in chunks:
                event = f"event: token\ndata: {json.dumps({'delta': chunk})}\n\n".encode("utf-8")
                self.wfile.write(event)
                self.wfile.flush()
                time.sleep(0.01)
            done = f"event: done\ndata: {json.dumps({'session_id': session_key, 'message_id': f'msg-{int(time.time()*1000)}'})}\n\n".encode("utf-8")
            self.wfile.write(done)
            self.wfile.flush()
            self.close_connection = True
            return

        self._send_json(404, {"error": "not_found"})

    def log_message(self, format: str, *args) -> None:
        return


def main() -> None:
    parser = argparse.ArgumentParser(description="TwinBench demo runtime fixture")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8090)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), DemoHandler)
    print(f"TwinBench demo runtime listening on http://{args.host}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
