PYTHON ?= $(shell command -v python3.10 2>/dev/null || command -v python3)
URL ?= http://localhost:8080
TOKEN ?=
USER_ID ?= 1
NAME ?= My Runtime

.PHONY: preflight run run-nullalis demo demo-docker site

preflight:
	bash scripts/preflight.sh "$(URL)" "$(TOKEN)" "$(USER_ID)"

run:
	bash scripts/run_twinbench.sh "$(URL)" "$(TOKEN)" "$(NAME)" "$(USER_ID)"

run-nullalis:
	bash scripts/run_twinbench_nullalis_local.sh

demo:
	$(PYTHON) -m harness.demo_runtime_fixture --host 127.0.0.1 --port 8090 & \
	DEMO_PID=$$!; \
	sleep 1; \
	bash scripts/run_twinbench_demo.sh http://127.0.0.1:8090 demo-internal-token "TwinBench Demo Runtime" demo-user; \
	kill $$DEMO_PID

demo-docker:
	docker compose up --build benchmark

site:
	$(PYTHON) scripts/build_website.py
