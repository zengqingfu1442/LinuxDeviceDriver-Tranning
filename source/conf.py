# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys, os
import datetime

sys.path.append(os.path.abspath('exts'))

project = 'LinuxDeviceDriver'
copyright = '2019-2024 深圳百问网科技有限公司'
author = '100ask_Team'
#release = '1.0'

master_doc = "index"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'myst_parser',
    'sphinx_design'

]

source_suffix = {
   '.rst': 'restructuredtext',  
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

myst_heading_anchors = 6
suppress_warnings = ["myst.header"]

# html_theme = 'alabaster'
html_theme = "sphinx_book_theme"
html_title = "Linux设备驱动开发教程中心"
html_copy_source = True
html_show_sourcelink = False
#html_logo = "_static/logo_binder.svg"
html_favicon = '_static/favicon.png'
html_last_updated_fmt = ""

html_sidebars = {
    '**': [
        "navbar-logo.html",
        "search-field.html",
        "sbt-sidebar-nav.html",
    ]
}

html_static_path = ['_static']

html_css_files = ['topbar.css', 'custom-theme.css']

locale_dirs = ['locale']

html_theme_options = {
    'collapse_navigation': True,
    "repository_url": "https://github.com/100askTeam/LinuxDeviceDriver-Tranning",
    'navigation_depth': 7,
    "use_repository_button": True,
    "announcement": (
        "📢📢📢 欢迎来到百问网Linux设备驱动开发教程中心文档站点！！！"
        "技术交流社区：https://forums.100ask.net"
    ),
    #"primary_sidebar_end": ["versionsFlex.html"],
}
