# Changelog

All notable changes to TwinBench should be documented in this file.

The format is intentionally simple and release-oriented.

## [0.2.1] - 2026-03-24

### Added

- Trust model documentation in `docs/TRUST_MODEL.md`
- Nullalis reference-runtime explainer in `docs/NULLALIS_REFERENCE_RUNTIME.md`
- Example run manifest in `docs/run-manifest-v0.2.example.json`
- Evidence parsing helpers in `harness/evidence.py`
- Open-source release checklist in `docs/OPEN_SOURCE_RELEASE_CHECKLIST.md`

### Changed

- Updated result submission template to require v0.2-style verified/projected reporting
- Updated README and CONTRIBUTING flow around trusted evidence packs
- Hardened chat transport for runtimes that require explicit `session_key`
- Isolated harness chat sessions per dimension
- Improved autonomy scoring to use diagnostics and metrics more directly
- Improved execution scoring with diagnostics-backed scheduler confirmation
- Improved breadth scoring with runtime_info-backed structured counts
- Reduced cross-channel reliance on generic assistant self-report

### Notes

- This release is focused on benchmark trust, open-source readiness, and compatibility with the current Nullalis gateway contract.

## [0.3.0] - 2026-03-25

### Added

- Public-facing TwinBench branding for personal AI assistant runtimes
- New newcomer docs: getting started, run profiles, preflight, compatibility checklist, glossary, integration paths, and lightweight submission flow
- Public results index and press kit
- Outreach packet and outreach target list for competitor and lab wave
- Dimension-level artifact status and reason code fields

### Changed

- Reframed README and specification around personal AI assistant runtime language
- Clarified scale fairness: same-session contention is diagnostic, multi-user fanout should provision users first
- Updated trust model and issue template to distinguish unavailable dimensions from product failure
- Added provisioning-aware scale benchmark behavior and Nullalis local token discovery flow
