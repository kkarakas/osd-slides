# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sphinx

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'osd-slides'
copyright = '2023, Kutay Karakas'
author = 'Kutay Karakas'
release = '0.2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", 'sphinx.ext.autodoc', "sphinx.ext.autodoc", "sphinx.ext.napoleon"] #FIXME
source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']
# import sphinx_rtd_theme
# html_theme = "sphinx_rtd_theme"
html_theme = 'agogo'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# def setup(app):
#     app.add_config_value('recommonmark_config', {
#         'auto_toc_tree_section': 'Contents',
#     }, True)
#     app.add_transform(AutoStructify)
import sys
import os
sys.path.insert(0, os.path.abspath('../'))