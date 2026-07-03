import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "GeoBrain"
author = "Anna Teruel-Sanchis and Konrad Danielewski"
copyright = "2026, Anna Teruel-Sanchis, Konrad Danielewski"

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

autosummary_generate = True
autodoc_member_order = "bysource"

nb_execution_mode = "off"

myst_heading_anchors = 3

templates_path = ["_templates"]

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/anna-teruel/geobrain",
}

html_logo = "_static/GeoBrain_logo1.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_sidebars = {
    "user_guides": ["sidebar-nav-bs.html", "page-toc.html"],
}
