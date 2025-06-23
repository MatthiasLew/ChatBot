# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

html_static_path = ['_static']
project = 'ChatBot'
copyright = '2025, Mateusz Lewandowski , Marek Sikora'
author = 'Mateusz Lewandowski , Marek Sikora'
release = '23.06.2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      # generowanie dokumentacji z docstringów
    'sphinx.ext.napoleon',     # obsługa Google/NumPy docstringów
    'sphinx.ext.viewcode',     # linki do kodu źródłowego
    'sphinxcontrib.plantuml',  # wstawianie diagramów PlantUML
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
