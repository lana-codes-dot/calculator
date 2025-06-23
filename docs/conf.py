"""Sphinx configuration."""
project = "calculatir"
author = "Roksolana K."
copyright = "2025, Roksolana K."
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
