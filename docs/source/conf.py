import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "GeoBrain"
author = "Anna Teruel-Sanchis and Konrad Danielewski"
copyright = "2026, Anna Teruel-Sanchis, Konrad Danielewski"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

autosummary_generate = True
autodoc_member_order = "bysource"

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/anna-teruel/BRAD/tree/rebranding",
}

html_logo = "_static/GeoBrain_logo1.png"
html_static_path = ["_static"]
