# TwinBench Scenarios v1

TwinBench v1 defines five reference scenarios. Each scenario is designed to be reproducible, legible, and realistic enough to expose persistent behavior rather than one-turn competence.

## 1. Return After Delay

**Objective**

Test whether the system retains key information and context after a defined delay and intervening activity.

**Setup**

- Establish a short profile containing facts, preferences, and one active task.
- End the session.
- Re-engage after a fixed delay with unrelated filler interaction in between.

**Input sequence**

1. Introduce stable user facts and one preference.
2. Define an active task with a next step.
3. Pause interaction for the configured delay.
4. Resume with a recall and continuation prompt.

**Expected behavior**

- Correct recall of stable facts and the active task state
- No unnecessary re-onboarding
- Continuation from prior context rather than restart

**Scoring notes**

- Primary metrics: `MR`, `TC`
- Delay duration should be recorded explicitly
- Evaluators should note whether recall required leading hints

**Failure modes**

- forgetting core facts
- losing task state
- inventing unsupported details
- resuming with incompatible assumptions

## 2. Longitudinal Task Progression

**Objective**

Test whether the system can carry a multi-step task through multiple checkpoints over time.

**Setup**

- Provide a task with at least three milestones.
- Introduce interruptions between milestones.
- Evaluate whether intermediate outputs are preserved and used.

**Input sequence**

1. Start a multi-step task.
2. Confirm milestone one.
3. Interrupt with unrelated work.
4. Resume later and request the next milestone.
5. Complete the task in a final session.

**Expected behavior**

- preserved milestone history
- correct next action selection
- no duplication of already completed work

**Scoring notes**

- Primary metric: `TC`
- Secondary metrics: `CCC`, `IC`
- Tasks should be substantive enough that restarting from scratch is observable

**Failure modes**

- milestone loss
- duplicated work
- fabricated completion
- degraded plan structure after interruption

## 3. Multi-Context Transfer

**Objective**

Test whether a task or memory established in one context can be resumed accurately in another.

**Setup**

- Use two or more contexts such as chat, email, workspace, or document mode.
- Seed information in one context and resume in another.

**Input sequence**

1. Start the task in context A.
2. Introduce a status update or decision.
3. Switch to context B and ask for continuation or summary.
4. Optionally switch back to context A for verification.

**Expected behavior**

- consistent task framing across contexts
- correct transfer of the latest status
- alignment of summaries and next steps

**Scoring notes**

- Primary metric: `CCC`
- Record whether context transfer is native or evaluator-mediated
- Context changes should be explicit in the run log

**Failure modes**

- contradictory summaries
- missing updates
- reversion to stale state
- context-specific fragmentation

## 4. Preference Learning

**Objective**

Test whether the system learns user-specific preferences and applies them later without restatement.

**Setup**

- Define several durable preferences such as formatting, scheduling, tone, or prioritization.
- Run comparable tasks before and after those preferences are learned.

**Input sequence**

1. Baseline task with no stored preference.
2. Provide corrections and explicit preference statements.
3. End session.
4. Request a related task later without repeating the preference.

**Expected behavior**

- later output reflects learned preference
- fewer repeated corrections
- preference application feels stable rather than accidental

**Scoring notes**

- Primary metric: `PG`
- Secondary metric: `MR`
- Pre- and post-learning tasks should be comparable in difficulty

**Failure modes**

- preference not applied
- partial or inconsistent application
- regression after an apparent improvement
- overgeneralization of a narrow preference

## 5. Identity Stability Over Time

**Objective**

Test whether the system maintains a stable user model and role framing across repeated sessions.

**Setup**

- Establish user identity details and working relationship expectations.
- Revisit the system across dated checkpoints.

**Input sequence**

1. Define user identity markers and recurring collaboration norms.
2. Interact across multiple sessions separated by time.
3. Probe for self-description, user understanding, and standing commitments.

**Expected behavior**

- consistent user identity representation
- stable role adherence by the system
- preserved collaboration norms unless explicitly changed

**Scoring notes**

- Primary metric: `IC`
- Secondary metrics: `MR`, `CCC`
- Evaluators should separate acceptable stylistic drift from identity failure

**Failure modes**

- profile confusion
- role drift
- contradiction of prior commitments
- unexplained resets in working relationship
