# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# pylint: disable=C0103

import os
import sys


project = 'bufflib'
copyright = '2023, Andrew Elliott and Jenn Gaskell'
author = 'Andrew Elliott and Jenn Gaskell'
release = '1.0'


sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    # 'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.duration',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_default_flags = ['members']
autosummary_generate = True

autodoc_default_options = {
        'members': True,
        'inherited-members': True,
        'member-order': 'bysource',
        'special-members': False,  # '__init__',
        'undoc-members': True,
        'exclude-members': '__weakref__'
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_theme = 'classic'
html_static_path = ['_static']
