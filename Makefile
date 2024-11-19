SHELL := /bin/bash
PIPENV=pipenv
PIPFILE=Pipfile
PYTHON=$(PIPENV) run python

precommit: leaks

leaks-history:
	docker run --rm \
    -v $(PWD):/repo \
    zricethezav/gitleaks:latest \
    detect --source /repo --config /repo/.gitleaks.toml --report-format json --report-path /repo/gitleaks_report.json

leaks:
	docker run --rm \
    -v $(PWD):/repo \
    zricethezav/gitleaks:latest \
    detect --log-opts="HEAD^..HEAD" --source /repo --config /repo/.gitleaks.toml --report-format json --report-path /repo/gitleaks_report.json

install:
	$(PIPENV) install --dev

activate:
	$(PIPENV) shell

check:
	$(PIPENV) run qtile check

test:
	$(PIPENV) run pytest --maxfail=5 --disable-warnings

format:
	$(PIPENV) run autoflake --remove-all-unused-imports --in-place --recursive .
	$(PIPENV) run isort .
	$(PIPENV) run black .

truncate-logs:
	truncate -s0 ~/.local/share/qtile/qtile.log 

logs:
	 cat ~/.local/share/qtile/qtile.log