SHELL := /bin/bash
PIPENV = pipenv
PIPFILE = Pipfile
PYTHON = $(PIPENV) run python

# Precommit hooks
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
	$(PIPENV) run pytest --cov=ebenezer --cov-report=term-missing --maxfail=5 --disable-warnings $(file)  $(args)

format:
	$(PIPENV) run autoflake --remove-all-unused-imports --in-place --recursive .
	$(PIPENV) run isort .
	$(PIPENV) run black .

clean:
	-rm -rf dist qtile.egg-info docs/_build build/ .tox/ .mypy_cache/ .pytest_cache/ .eggs/

truncate-logs:
	truncate -s0 ~/.local/share/qtile/qtile.log 

logs:
	cat ~/.local/share/qtile/qtile.log

docs-clean:
	rm -rf docs/_build docs/_static
	mkdir -p docs/_build docs/_static

docs-locally:
	$(MAKE) docs-clean
	$(PIPENV) run sphinx-apidoc -o docs ebenezer/
	$(PIPENV) run sphinx-build -b html docs docs/_build/html

deploy:
	rm -rf dist/*
	$(PIPENV) run bump2version patch
	$(PIPENV) run python setup.py sdist bdist_wheel
	$(PIPENV) run twine upload dist/*

test:
	$(PIPENV) run pytest

.PHONY: precommit leaks-history leaks truncate-logs logs docs-clean docs-locally deploy test install clean