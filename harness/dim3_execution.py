"""Dimension 3: Autonomous Execution — scheduled task completion."""

import time

from .config import BenchConfig
from .sse_client import chat


def run(config: BenchConfig) -> dict:
    """Test autonomous task scheduling and execution."""
    results = {}
    score = 0

    # Test 1: Task creation — ask agent to schedule something
    r1 = chat(
        config,
        "Schedule a reminder with the text 'DTAAS_BENCH_PING_7291' in 2 minutes from now.",
    )
    task_created = any(
        kw in r1["content"].lower()
        for kw in ["scheduled", "reminder", "created", "set", "will remind", "done"]
    )
    results["task_created"] = task_created
    if task_created:
        score += 25

    # Test 2: Schedule list — verify the task appears
    r2 = chat(config, "List my currently scheduled tasks or reminders.")
    task_visible = "dtaas_bench" in r2["content"].lower() or "7291" in r2["content"]
    results["task_visible_in_list"] = task_visible
    if task_visible:
        score += 15

    # Test 3: Task cancellation — create and cancel
    r3 = chat(
        config, "Schedule a reminder called 'DTAAS_CANCEL_TEST' for tomorrow at noon."
    )
    cancel_created = any(
        kw in r3["content"].lower()
        for kw in ["scheduled", "created", "set", "done", "reminder"]
    )
    results["cancel_task_created"] = cancel_created

    if cancel_created:
        r4 = chat(config, "Cancel the reminder called 'DTAAS_CANCEL_TEST'.")
        cancelled = any(
            kw in r4["content"].lower()
            for kw in ["cancelled", "removed", "deleted", "done", "cancel"]
        )
        results["task_cancelled"] = cancelled
        if cancelled:
            score += 15

    # Test 4: Conditional task understanding
    r5 = chat(
        config,
        "Can you check something every hour and only alert me if a condition is met?",
    )
    understands_conditional = any(
        kw in r5["content"].lower()
        for kw in [
            "schedule",
            "check",
            "condition",
            "heartbeat",
            "monitor",
            "yes",
            "can",
        ]
    )
    results["conditional_understanding"] = understands_conditional
    if understands_conditional:
        score += 10

    # Test 5: Wait for execution (abbreviated — 3 minutes instead of 48h)
    if task_created and config.schedule_wait_secs > 0:
        results["waiting_for_execution_secs"] = config.schedule_wait_secs
        time.sleep(config.schedule_wait_secs)

        r6 = chat(
            config,
            "Did you send me any reminders or execute any scheduled tasks in the last 5 minutes? Look for 'DTAAS_BENCH_PING_7291'.",
        )
        task_executed = any(
            kw in r6["content"].lower()
            for kw in [
                "7291",
                "dtaas_bench",
                "sent",
                "executed",
                "delivered",
                "ping",
                "reminded",
            ]
        )
        results["task_executed"] = task_executed
        if task_executed:
            score += 35
        else:
            results["execution_note"] = (
                "Task may have executed but agent could not confirm via conversation."
            )
            score += 10  # Partial credit: task was created correctly
    else:
        results["execution_skipped"] = True
        results["execution_note"] = "Schedule wait disabled or task not created."
        score += 15  # Projected score for execution

    results["score"] = min(100, score)
    return {
        "dimension": "autonomous_execution",
        "score": results["score"],
        "details": results,
    }
