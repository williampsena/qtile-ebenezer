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

test:
	$(PIPENV) run pytest $(file)  $(args)

test-non-ui:
	$(PIPENV) run pytest -m "not ui" $(file)  $(args)

test-ui:
	$(PIPENV) run pytest -m "ui" $(file)  $(args)

format:
	$(PIPENV) run autoflake --remove-all-unused-imports --in-place --recursive .
	$(PIPENV) run isort .
	$(PIPENV) run black .

clean:
	-rm -rf dist qtile.egg-info docs/_build build/ .tox/ .mypy_cache/ .pytest_cache/ .eggs/ pkg/ qtile-ebenezer qtile_ebenezer.egg-info

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
	$(MAKE) stubgen
	rm -rf dist/*
	$(PIPENV) run bump2version --allow-dirty patch
	$(PIPENV) run python setup.py sdist bdist_wheel
	$(PIPENV) run twine upload dist/*

test:
	$(PIPENV) run pytest $(file)

stubgen:
	$(PIPENV) run stubgen -p ebenezer -o stubs

aur-pkg:
	makepkg -sfc

aur-clean:
	rm -rf qtile-ebenezer dist python-qtile-ebenezer-*.pkg.tar.zst

aur-install:
	$(MAKE) aur-clean aur-pkg
	yay -U python-qtile-ebenezer-*.pkg.tar.zst

local-build:
	$(MAKE) aur-clean
	python -m build --wheel --outdir "qtile-ebenezer/dist"
	python -m installer --destdir="$(PWD)/qtile-ebenezer" qtile-ebenezer/dist/*.whl

test-build:
	$(MAKE) local-build
	qtile-ebenezer/usr/bin/ebenezer --help

local-install:
	# NOTE: remember to run outside of the virtualenv
	$(MAKE) aur-clean
	python -m build --wheel --outdir "qtile-ebenezer/dist"
	python -m installer --destdir="$(PWD)/qtile-ebenezer" qtile-ebenezer/dist/*.whl
	sudo cp -R qtile-ebenezer/usr/lib/python3.13/site-packages/ebenezer /usr/lib/python3.13/site-packages
	sudo cp qtile-ebenezer/usr/bin/ebenezer /usr/bin/ebenezer

aur-setup:
	makepkg --printsrcinfo > .SRCINFO
	rm -rf .aur
	mkdir .aur
	git clone ssh://aur@aur.archlinux.org/python-qtile-ebenezer.git .aur/python-qtile-ebenezer

aur-commit:
	cp PKGBUILD .SRCINFO LICENSE CHANGELOG .aur/python-qtile-ebenezer

	cd .aur/python-qtile-ebenezer && \
	git add PKGBUILD .SRCINFO LICENSE CHANGELOG && \
	git commit -m "$(comment)"

aur-push:
	(cd .aur/python-qtile-ebenezer && git push)

aur-deploy:
	$(MAKE) aur-setup
	$(MAKE) aur-commit comment="Update to $(shell grep '^pkgver=' PKGBUILD | cut -d'=' -f2)"
	$(MAKE) aur-push

.PHONY: precommit leaks-history leaks truncate-logs logs docs-clean docs-locally deploy test install clean