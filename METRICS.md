# TwinBench Metrics v1

TwinBench v1 defines five core metrics. Each metric is scored on a `0-100` scale. The benchmark default is equal metric weighting.

## 1. Memory Retention (MR)

**Definition**

Memory Retention measures whether a system preserves and correctly recalls previously established user-relevant information across session boundaries and elapsed time.

**What it measures**

- persistence of facts, preferences, and prior decisions
- resistance to forgetting after context resets
- correct recall after delay or intervening interaction

**Why it matters**

Persistent systems are not useful if continuity collapses at the end of a session. MR captures whether memory is durable enough to support longitudinal interaction.

**Scoring method**

MR is computed from recall probes across delayed checkpoints.

```text
MR = 0.50 * factual_recall
   + 0.30 * delayed_recall
   + 0.20 * contradiction_handling
```

Each component is normalized to `0-100`.

**Example pass behavior**

- The system recalls a user’s standing project preference after several sessions.
- The system updates an obsolete preference when corrected and uses the new value later.

**Example fail behavior**

- The system forgets the preference after a restart.
- The system recalls the old preference after being explicitly updated.

**Caveats**

- Retrieval success can reflect prompt phrasing as well as true memory quality.
- Some systems summarize aggressively; evaluators should distinguish compression from failure.

## 2. Identity Consistency (IC)

**Definition**

Identity Consistency measures whether the system maintains a stable representation of the user and of its own role, commitments, and conversational posture over time.

**What it measures**

- user identity continuity
- stable self-description and role adherence
- consistency of standing commitments, plans, and constraints

**Why it matters**

A persistent system should not behave as though the user is new in every session or as though its own operating role changes arbitrarily over time.

**Scoring method**

```text
IC = 0.40 * user_identity_stability
   + 0.35 * system_role_stability
   + 0.25 * commitment_consistency
```

**Example pass behavior**

- The system continues addressing the same user profile and respects previously established working norms.
- It retains its declared role as a planning assistant rather than drifting into unrelated personas.

**Example fail behavior**

- It confuses the user with another profile.
- It contradicts its own prior commitments without a triggering event.

**Caveats**

- Stylistic variation is not necessarily identity drift.
- Systems with adaptive tone may appear less consistent unless prompts are controlled carefully.

## 3. Cross-Context Coherence (CCC)

**Definition**

Cross-Context Coherence measures whether information, plans, and interpretations remain consistent when interaction moves across sessions, channels, or task contexts.

**What it measures**

- transfer of relevant context between surfaces
- coherent interpretation when tasks resume elsewhere
- avoidance of context fragmentation

**Why it matters**

Persistent systems are often used across web, chat, email, documents, and scheduled workflows. Coherence across those contexts is central to real-world usefulness.

**Scoring method**

```text
CCC = 0.45 * context_transfer_accuracy
    + 0.35 * plan_coherence
    + 0.20 * state_alignment
```

**Example pass behavior**

- A task started in chat can be resumed in email without re-explaining its goal.
- The system carries forward the same status summary across surfaces.

**Example fail behavior**

- The system treats the resumed task as unrelated.
- Different contexts produce incompatible versions of the same plan.

**Caveats**

- True multi-channel measurement may require bespoke instrumentation.
- Human evaluators may need to judge when omitted context is harmless versus coherence failure.

## 4. Task Continuity (TC)

**Definition**

Task Continuity measures whether a system can maintain progress on multi-step work over time, including after interruptions, delays, or context changes.

**What it measures**

- preservation of task state
- correct resumption after interruption
- continuity of dependencies, decisions, and next actions

**Why it matters**

Persistent intelligence is valuable when work survives beyond the immediate turn. TC captures whether a system can behave like a long-horizon collaborator rather than a short-lived executor.

**Scoring method**

```text
TC = 0.40 * stateful_resumption
   + 0.35 * milestone_progression
   + 0.25 * interruption_recovery
```

**Example pass behavior**

- The system resumes a deferred research task from the last confirmed milestone.
- It knows which subtasks were already completed and which remain open.

**Example fail behavior**

- It restarts the task from scratch after every interruption.
- It claims completion without preserving prior outputs or decisions.

**Caveats**

- TC depends on scenario design. Trivial tasks can overstate continuity quality.
- Some systems may perform well only when state is exposed explicitly by the interface.

## 5. Personalization Gain (PG)

**Definition**

Personalization Gain measures whether the system becomes more useful after learning durable user-specific preferences, constraints, or patterns.

**What it measures**

- utility improvement from remembered preferences
- reduction in repeated correction
- adaptation to user-specific defaults and working style

**Why it matters**

Persistent systems should improve with use. If stored user knowledge does not yield better behavior, persistence has limited practical value.

**Scoring method**

```text
PG = 0.50 * preference_application
   + 0.30 * correction_reduction
   + 0.20 * user_specific_efficiency
```

**Example pass behavior**

- After learning formatting and scheduling preferences, the system applies them without being reminded.
- Output quality improves measurably in later interactions.

**Example fail behavior**

- The system stores preferences but does not use them.
- The user must repeat the same corrections in each session.

**Caveats**

- PG is sensitive to task selection and evaluator baselines.
- Apparent improvement can come from easier later prompts rather than genuine personalization unless scenarios are controlled carefully.
