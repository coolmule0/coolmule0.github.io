#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'John Charlton'
SITENAME = 'John Charlton'
SITEURL = ''
# SITEURL = 'https://coolmule0.github.io'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('RSE Sheffield', 'https://rse.shef.ac.uk/'),)

# Social widget
SOCIAL = (('Email', 'mailto:j.a.charlton@sheffield.ac.uk'),
          ('Github', 'https://github.com/coolmule0"'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'static'
]

ARTICLE_PATHS = [
    'Articles',
]

PAGE_EXCLUDES = [
    'static'
]

ARTICLE_EXCLUDES = [
    'static'
]



DISPLAY_CATEGORIES_ON_MENU = False

TEMPLATE_PAGES = {

}

AUTHOR_SAVE_AS = ''