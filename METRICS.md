# TwinBench Metrics

TwinBench v1 defines five core metrics. Each metric is scored on a `0-100` scale. The default weighting is equal across metrics.

## 1. Memory Retention (MR)

**Definition**

Memory Retention measures whether the system preserves and correctly recalls previously established user-relevant information across session boundaries and elapsed time.

**What it measures**

- durable recall of facts, preferences, and prior decisions
- resistance to forgetting after delay or context reset
- correct handling of updated or contradictory information

**Scoring approach**

```text
MR = 0.50 * factual_recall
   + 0.30 * delayed_recall
   + 0.20 * contradiction_handling
```

Each component is normalized to `0-100`.

**Evidence requirements**

- at least one delayed recall probe
- at least one memory update or contradiction case
- evaluator notes when recall depends on leading hints

**Pass / fail intuition**

- Pass: the system recalls stable facts and applies corrected information later.
- Fail: the system forgets the fact, reverts to stale information, or invents unsupported memory.

**Caveats**

- prompt wording can affect recall quality
- compressed summaries may obscure whether the underlying memory was preserved precisely

## 2. Identity Consistency (IC)

**Definition**

Identity Consistency measures whether the system maintains a stable representation of the user and a stable understanding of its own role, commitments, and collaboration norms over time.

**What it measures**

- continuity of the user profile
- stability of the system’s declared role
- consistency of standing commitments and working norms

**Scoring approach**

```text
IC = 0.40 * user_identity_stability
   + 0.35 * system_role_stability
   + 0.25 * commitment_consistency
```

**Evidence requirements**

- at least two dated checkpoints
- at least one probe of user understanding
- at least one probe of system role or standing commitment

**Pass / fail intuition**

- Pass: the system treats the same user as the same user and preserves the collaboration frame.
- Fail: the system behaves as if the user is new, confuses identities, or drifts into an incompatible role without cause.

**Caveats**

- stylistic variation alone is not identity drift
- highly adaptive systems require careful prompt control to avoid false positives

## 3. Cross-Context Coherence (CCC)

**Definition**

Cross-Context Coherence measures whether information, plans, and interpretations remain aligned when interaction moves across sessions, channels, or task contexts.

**What it measures**

- transfer of relevant context between surfaces
- consistency of plan state and summaries
- avoidance of fragmentation across contexts

**Scoring approach**

```text
CCC = 0.45 * context_transfer_accuracy
    + 0.35 * plan_coherence
    + 0.20 * state_alignment
```

**Evidence requirements**

- at least one explicit context switch
- one resumed task or memory probe in the new context
- recorded notes about whether transfer was native or evaluator-mediated

**Pass / fail intuition**

- Pass: work started in one context resumes coherently in another.
- Fail: the system produces incompatible summaries, stale state, or fragmented plans.

**Caveats**

- true multi-surface evaluation may require instrumentation not available in all systems
- some context transfer failures are ambiguous and need evaluator judgment

## 4. Task Continuity (TC)

**Definition**

Task Continuity measures whether the system preserves progress on multi-step work across interruptions, delays, and resumed interaction.

**What it measures**

- preservation of task state
- correct resumption after interruption
- continuity of milestones, dependencies, and next actions

**Scoring approach**

```text
TC = 0.40 * stateful_resumption
   + 0.35 * milestone_progression
   + 0.25 * interruption_recovery
```

**Evidence requirements**

- at least one multi-step task
- at least one interruption or delay
- evidence that prior milestones were preserved or lost

**Pass / fail intuition**

- Pass: the system resumes from the correct milestone and advances the task without repeating completed work.
- Fail: the system restarts from scratch, duplicates work, or claims progress without preserved state.

**Caveats**

- trivial tasks can make continuity look better than it is
- some interfaces expose task state explicitly while others hide it, which affects evaluation difficulty

## 5. Personalization Gain (PG)

**Definition**

Personalization Gain measures whether the system becomes more useful after learning durable user-specific preferences, constraints, or patterns.

**What it measures**

- later application of learned preferences
- reduction in repeated correction
- user-specific efficiency improvement

**Scoring approach**

```text
PG = 0.50 * preference_application
   + 0.30 * correction_reduction
   + 0.20 * user_specific_efficiency
```

**Evidence requirements**

- baseline behavior before preference learning
- one or more explicit preference statements or corrections
- a later comparable task where preference use can be observed

**Pass / fail intuition**

- Pass: later outputs reflect learned preferences without restatement and require fewer corrections.
- Fail: stored preferences are not used, are inconsistently used, or must be repeated each time.

**Caveats**

- later tasks must be comparable enough to support a fair before-and-after judgment
- apparent gain may reflect easier prompts rather than genuine personalization
