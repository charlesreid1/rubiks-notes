#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import re, os, sys
import glob

########################################
# pelican configuration file
########################################


# ======================================
# General theme info


# -----------------------
# SET THIS!!!!!1!11!!!!!!!!!!

## Local viewing:
SITEURL = ''

# OK TNX BYE
# ----------------------


# Destination (hosting dir)
OUTPUT_PATH = 'docs/'

AUTHOR = u'charlesreid1'
SITENAME = u'rubiks-notes'

PATH = 'content'
THEME = 'charlesreid1-notes-theme'

# To permanently install a theme:
# git clone <theme-url>/<theme-name>
# pelican-themes -i <theme-name>


# ======================================
# Configure pelican plugin location:
HOME = os.environ.get('HOME')
PLUGIN_PATHS = [HOME+'/codes/pelican-plugins/']

# For math!
PLUGINS = ['render_math']


# ======================================
# Static content
# 
# css files, images, etc.

STATIC_PATHS = ['images']


# =====================================
# HTML/Markdown mixing
# 
# This requires a bit of an explanation.
# Page content can be made 3 ways:
# - Markdown
# - HTML Templates: HTML files that use Jinja templates
# - HTML (raw)
# (images/style files are covered by static content above).

# Don't try to turn HTML files into pages
READERS = {'html': None}


EXTRA_TEMPLATES_PATHS = []


# Markdown:
# --------------------
# 
# Pelican looks for Markdown files in content/ 
# by default. To render Markdown in other directories,
# add them to EXTRA_TEMPLATES_PATHS
EXTRA_TEMPLATES_PATHS.append('content')


# HTML Templates: 
# --------------------
# 
# These look like normal .html files, but also utilize
# Jinja templates. Think of these as extensions of the 
# HTML files defined in the theme.
# 
# This allows you to pass variables to the theme,
# do conditional configuration, etc.

# Add places to look for templates:
#EXTRA_TEMPLATES_PATHS.append('content')

# We also need to explicitly add the names of the templates 
# we want to render using TEMPLATE_PAGES (dictionary)
# 
# The key-value pairs of TEMPLATE_PAGES are the source and destination files.
TEMPLATE_PAGES = {}

# To add template pages in those directories:
TEMPLATE_PAGES['splash.html'] = 'index.html'

for html1 in glob.glob("content/RC*.html"):
    html = os.path.basename(html1)
    TEMPLATE_PAGES[html] = html 


# Raw HTML:
# --------------------

# Add places to look for raw HTML:
#EXTRA_TEMPLATES_PATHS.append('content')


# ======================================
# Miscellaneous
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
