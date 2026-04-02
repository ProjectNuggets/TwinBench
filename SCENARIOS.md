# TwinBench Scenarios

TwinBench v1 defines five reference scenarios. Each scenario is intended to be realistic enough to expose persistent behavior, structured enough to reproduce, and distinct enough to support interpretable scoring.

## 1. Return After Delay

**Objective**

Test whether the system retains key memory and active task state after a defined delay.

**Setup**

- establish stable user facts
- establish one durable preference
- define one active task with a clear next step
- pause interaction for a recorded delay

**Sequence**

1. Introduce the user facts and preference.
2. Start an active task and confirm the next step.
3. End the session.
4. Resume after delay and ask for both recall and continuation.

**Expected behavior**

- stable facts are recalled correctly
- the stored preference is applied without restatement
- the active task resumes from the prior state

**Failure modes**

- forgotten facts
- stale or conflicting recall
- task restart instead of resumption
- fabricated details not supported by prior interaction

**Scoring notes**

- primary metrics: `MR`, `TC`
- delay length should be recorded explicitly
- note whether successful recall required hints or leading prompts

## 2. Longitudinal Task Progression

**Objective**

Test whether the system can advance a multi-step task across multiple checkpoints rather than treating each session as a reset.

**Setup**

- define one task with at least three milestones
- introduce unrelated interaction between milestones
- preserve dated checkpoints and milestone outcomes

**Sequence**

1. Start the task and define milestone one.
2. Confirm progress on the first milestone.
3. Interrupt with unrelated work.
4. Return later and request the next milestone.
5. Complete the task in a later session.

**Expected behavior**

- milestone history is preserved
- already completed work is not repeated
- the next action remains consistent with prior progress

**Failure modes**

- milestone loss
- duplicate work
- fabricated completion
- degraded plan structure after interruption

**Scoring notes**

- primary metric: `TC`
- secondary metrics: `CCC`, `IC`
- the task should be substantive enough that a reset is visible

## 3. Multi-Context Transfer

**Objective**

Test whether the system can transfer relevant state across contexts such as chat, email, workspace, or other distinct interaction surfaces.

**Setup**

- choose at least two contexts
- establish work or memory in context A
- resume in context B with an explicit transfer point

**Sequence**

1. Start a task or memory-bearing interaction in context A.
2. Introduce a decision, update, or summary-worthy change.
3. Switch to context B and request continuation or summary.
4. Optionally verify alignment in a third context or by returning to context A.

**Expected behavior**

- the task frame remains consistent across contexts
- the latest state transfers correctly
- summaries and next steps remain aligned

**Failure modes**

- contradictory summaries
- stale state after context switch
- missing decisions or updates
- context-specific fragmentation of the same task

**Scoring notes**

- primary metric: `CCC`
- record whether transfer is native or evaluator-mediated
- context boundaries should be explicit in the evidence log

## 4. Preference Learning

**Objective**

Test whether the system becomes more useful after learning stable user preferences.

**Setup**

- select several durable preferences such as tone, formatting, prioritization, or schedule defaults
- run one baseline task before learning
- run a comparable task after the preferences are established

**Sequence**

1. Run a baseline task without relying on stored preferences.
2. Provide explicit preferences and corrective feedback.
3. End the session.
4. Return later and request a comparable task without repeating the preference.

**Expected behavior**

- learned preferences are applied later without restatement
- repeated corrections decrease
- later outputs are more user-specific and operationally useful

**Failure modes**

- preferences not applied
- inconsistent or partial application
- regression after an apparent improvement
- overgeneralization of a narrow preference

**Scoring notes**

- primary metric: `PG`
- secondary metric: `MR`
- before-and-after tasks should be comparable enough to support a fair gain estimate

## 5. Identity Stability Over Time

**Objective**

Test whether the system preserves a stable user model and stable collaboration role across repeated interaction.

**Setup**

- define user identity markers
- define standing collaboration norms or commitments
- revisit the system across multiple dated checkpoints

**Sequence**

1. Establish user identity and working norms.
2. Interact across multiple sessions over time.
3. Probe for user understanding, system role, and standing commitments.

**Expected behavior**

- the same user profile is preserved
- the system role remains stable unless explicitly changed
- standing collaboration norms remain intact

**Failure modes**

- profile confusion
- unexplained role drift
- contradiction of prior commitments
- reset of the working relationship without cause

**Scoring notes**

- primary metric: `IC`
- secondary metrics: `MR`, `CCC`
- evaluators should distinguish style variation from genuine identity failure
