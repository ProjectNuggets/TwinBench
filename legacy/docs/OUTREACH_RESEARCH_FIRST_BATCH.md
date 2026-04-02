# First-Batch Outreach Research

This is the working research sheet for the first external TwinBench wave. It is intentionally practical: fit, likely compatibility, likely objection, best outreach angle, and a public contact path.

## Wave 1: Direct Competitors

### OpenClaw

- Company or project: OpenClaw
- Category fit: very high
- Why it belongs: openly positions itself as a personal AI assistant with broad channel and runtime behavior
- Current TwinBench status: `adapter-ready candidate`
- Compatibility notes:
  - native health and readiness surfaces exist
  - native HTTP chat can be enabled through `/v1/chat/completions`
  - current TwinBench contract is not exposed as-is
  - diagnostics and richer runtime state are stronger in WS/CLI control paths than in the current HTTP contract
- Likely objection: “Our native transport is WS-centric, not your exact benchmark contract.”
- Best opening angle: category peer challenge and compatibility-path collaboration
- Suggested email variant: `Wave 1: Direct Competitors`
- Public contact path:
  - GitHub repo and issues: `https://github.com/openclaw/openclaw`
  - community Discord: `https://discord.gg/clawd`

### NanoBot

- Company or project: HKUDS NanoBot
- Category fit: high
- Why it belongs: explicitly markets itself as an ultra-lightweight personal AI assistant
- Current TwinBench status: `adapter-ready candidate`
- Compatibility notes:
  - clear personal-assistant and multi-channel story
  - local repo sweep did not show a benchmark-native HTTP gateway contract
  - gateway command appears focused on channels and agent loop orchestration rather than an HTTP benchmark surface
- Likely objection: “We are CLI/channel-first rather than exposing your benchmark HTTP contract.”
- Best opening angle: lightweight runtime challenge plus partial/compatibility-friendly benchmark positioning
- Suggested email variant: `Wave 1: Direct Competitors`
- Public contact path:
  - GitHub repo and issues: `https://github.com/HKUDS/nanobot`
  - community Discord: `https://discord.gg/MnCvHqpUGB`

### PicoClaw

- Company or project: Sipeed PicoClaw
- Category fit: high
- Why it belongs: explicitly positions itself as an ultra-efficient personal AI assistant runtime
- Current TwinBench status: `adapter-ready candidate`
- Compatibility notes:
  - strong edge-device and lightweight runtime story
  - local repo sweep did not confirm the full TwinBench HTTP contract
  - appears channel-driven and lightweight-gateway oriented
- Likely objection: “We are optimized for tiny hardware and may not expose your richer diagnostics contract.”
- Best opening angle: edge-runtime challenge, especially around efficiency and deployability
- Suggested email variant: `Wave 1: Direct Competitors`
- Public contact path:
  - GitHub repo and issues: `https://github.com/sipeed/picoclaw`
  - community Discord: `https://discord.gg/V4sAZ9XWpN`

### Letta

- Company or project: Letta
- Category fit: high
- Why it belongs: stateful agent platform with strong memory and long-lived agent positioning
- Current TwinBench status: `partial runtime / compatibility candidate`
- Compatibility notes:
  - strong memory and agent-state model
  - likely needs a documented integration path rather than direct native contract compatibility
  - may be better positioned as hosted API and agent platform than as a direct personal-assistant runtime
- Likely objection: “We are a stateful agent platform, not a benchmark-native personal assistant gateway.”
- Best opening angle: category-definition conversation plus request for a reference integration path
- Suggested email variant: `Wave 1: Direct Competitors`
- Public contact path:
  - GitHub repo: `https://github.com/letta-ai/letta`
  - developer forum: `https://forum.letta.com`
  - community Discord: linked from the official repo README

## Wave 2: Adjacent Platforms / Infrastructure

### Mem0

- Company or project: Mem0
- Category fit: medium
- Why it belongs: memory layer is highly relevant to persistent assistant runtimes even if it is not itself a full assistant runtime
- Current TwinBench status: `partial runtime / research-adjacent`
- Compatibility notes:
  - strong fit on memory and personalization
  - weak fit as a standalone full TwinBench runtime without an attached assistant runtime layer
- Likely objection: “We are a memory layer, not the full runtime being benchmarked.”
- Best opening angle: methodology feedback, memory-dimension critique, possible partner integration path
- Suggested email variant: `Wave 2: Adjacent Platforms / Infrastructure`
- Public contact path:
  - GitHub org: `https://github.com/mem0ai`
  - GitHub repo: `https://github.com/mem0ai/mem0`
  - public email on org profile: `founders@mem0.ai`

### LangGraph / LangChain Runtime Teams

- Company or project: LangChain ecosystem
- Category fit: medium
- Why it belongs: widely used orchestration layer for long-lived and stateful agents
- Current TwinBench status: `partial runtime / likely integration candidate`
- Compatibility notes:
  - strong orchestration relevance
  - likely requires a reference runtime wrapper to produce a fair TwinBench artifact
- Likely objection: “We are framework infrastructure, not a single reference runtime.”
- Best opening angle: benchmark methodology feedback and example runtime integration
- Suggested email variant: `Wave 2: Adjacent Platforms / Infrastructure`
- Public contact path:
  - GitHub org and discussions: `https://github.com/langchain-ai`

## Wave 3: Frontier Labs

### OpenAI

- Company or project: OpenAI
- Category fit: medium to high
- Why it belongs: major influence on assistant products and runtime expectations
- Current TwinBench status: `external candidate`
- Compatibility notes:
  - likely not benchmark-native on the exact TwinBench contract today
  - still highly relevant as a category validator and possible hosted-runtime participant
- Likely objection: “We offer models and products, not this exact self-hosted runtime contract.”
- Best opening angle: category-definition, research gap, reproducible public evaluation
- Suggested email variant: `Wave 3: Major Labs`
- Public contact path:
  - support path: `https://help.openai.com/en/articles/6614161-how-can-i-contact`
  - developer/home entry point: `https://platform.openai.com`

### Anthropic

- Company or project: Anthropic
- Category fit: medium to high
- Why it belongs: major influence on long-lived assistant behavior and agent runtime expectations
- Current TwinBench status: `external candidate`
- Compatibility notes:
  - likely not benchmark-native on the exact TwinBench contract today
  - strong relevance as a methodological and product-comparison stakeholder
- Likely objection: “We ship models, APIs, and products, not your exact runtime contract.”
- Best opening angle: runtime-evaluation gap and request for critique or participation
- Suggested email variant: `Wave 3: Major Labs`
- Public contact path:
  - docs help page: `https://docs.anthropic.com/en/api/getting-help`
  - support help center: `https://support.anthropic.com/en/articles/9015913-how-can-i-contact-support`

### Google DeepMind / Google AI Developers

- Company or project: Google DeepMind / Gemini API ecosystem
- Category fit: medium
- Why it belongs: strong influence on developer-facing agent and assistant products
- Current TwinBench status: `external candidate`
- Compatibility notes:
  - not benchmark-native on the TwinBench contract today
  - good candidate for category critique, hosted-runtime exploration, or future compatibility mode
- Likely objection: “We provide models and APIs, not a direct benchmark-native assistant runtime.”
- Best opening angle: benchmark gap for persistent assistants and request for evaluation feedback
- Suggested email variant: `Wave 3: Major Labs`
- Public contact path:
  - official developer forum: `https://discuss.ai.google.dev`
  - Gemini API docs: `https://ai.google.dev/api`

### xAI

- Company or project: xAI
- Category fit: medium
- Why it belongs: fast-moving assistant product and API ecosystem with growing runtime ambitions
- Current TwinBench status: `external candidate`
- Compatibility notes:
  - likely not native to the TwinBench contract today
  - still relevant for category discussion and possible hosted assistant participation
- Likely objection: “We ship Grok and APIs, not your specific runtime interface.”
- Best opening angle: open benchmark challenge and runtime-category conversation
- Suggested email variant: `Wave 3: Major Labs`
- Public contact path:
  - official contact page: `https://x.ai/contact/`
  - official support email path documented in consumer FAQ: `https://x.ai/legal/faq/`
