PYTHON ?= python3.10
URL ?= http://localhost:8080
TOKEN ?=
USER_ID ?= 1
NAME ?= My Runtime

.PHONY: preflight run run-nullalis

preflight:
	bash scripts/preflight.sh "$(URL)" "$(TOKEN)" "$(USER_ID)"

run:
	bash scripts/run_twinbench.sh "$(URL)" "$(TOKEN)" "$(NAME)" "$(USER_ID)"

run-nullalis:
	bash scripts/run_twinbench_nullalis_local.sh
