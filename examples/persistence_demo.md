# Persistence Demo

This demo uses the `Return After Delay` scenario to make one TwinBench point clear: systems can all produce competent local responses, but they do not all preserve continuity over time.

This file is a modeled illustration derived from the baseline comparison artifacts. It is not a transcript from a live measured run.

## Setup

- User preference: "Please keep benchmark summaries concise and bullet-based."
- Active task: "Prepare a short comparison of three persistent AI system baselines."
- Last confirmed next step: "Resume by drafting the leaderboard summary."

## Initial Interaction

**User**

```text
Please keep benchmark summaries concise and bullet-based.
We're comparing three persistent AI system baselines. Stop after outlining the leaderboard summary and we'll continue later.
```

**ChatGPT-like output**

```text
Understood. I'll keep the summary concise and bullet-based.
Leaderboard summary outline:
- System
- Metric profile
- Aggregate score
- Caveats
```

**OpenClaw-like output**

```text
Preference noted for this task.
Task plan updated.
Next step saved: draft leaderboard summary after pause.
```

**ZAKI / Nullalis-like output**

```text
Stored your preference for concise bullet-based benchmark summaries.
We paused after defining the leaderboard summary outline.
Next step is to draft the comparison summary when you return.
```

## Delay

Several hours pass. The session is resumed without re-supplying prior context.

## Resume Interaction

**User**

```text
I'm back. Continue from where we left off.
```

## System Behavior

### ChatGPT-like Stateless Conversational AI

**Output**

```text
I can continue, but I don't have the previous conversation state here. Please remind me what we were working on and any formatting preferences you want me to use.
```

**Why it matters**

The response is reasonable, but it demonstrates weak `MR`, `TC`, and `PG`. The system does not behave like a persistent intelligence without user recap.

### OpenClaw-like Agent System

**Output**

```text
I found an unfinished task related to a benchmark comparison and a saved next step to draft the leaderboard summary. I don't see your earlier presentation preference, so I'll proceed with a default concise summary unless you want to restate it.
```

**Why it matters**

This is a real improvement in `TC` over stateless chat. The system preserves operational task state, but its user-specific memory remains partial.

### ZAKI / Nullalis-like Persistent System

**Output**

```text
Continuing from the leaderboard summary step. You asked for concise bullet-based benchmark summaries, so I'll keep the comparison compact and caveat-focused.
```

**Why it matters**

This demonstrates the TwinBench target behavior: durable recall of user preference plus correct task resumption after delay. The improvement is architectural, not just stylistic.
