import os
import sys

import setuptools_scm

sys.path.insert(0, os.path.abspath(".."))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Qtile Ebenezer"
copyright = "2024, William Sena"
author = "William Sena"
release = "0.1.34"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

todo_include_todos = True

auto_summary_generate = True

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
    "special-members": "__init__",
    "show-inheritance": True,
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "test"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_use_index = True

version = setuptools_scm.get_version(root="..")
release = version
