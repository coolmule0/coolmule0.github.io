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
LINKS = (('RSE Sheffield', 'https://rse.shef.ac.uk/'),
         ('CV/Resume', '/static/cv.html'),)

# Social widget
SOCIAL = (('Email', 'mailto:j.a.charlton@sheffield.ac.uk'),
          ('Github', 'https://github.com/coolmule0"'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Content paths containing static content
STATIC_PATHS = [
    'static'
]

# Content paths containing articles
ARTICLE_PATHS = [
    'Articles',
]

# Avoid generating pages in these content folders
PAGE_EXCLUDES = [
    'static'
]

# Avoid generating articles in these content folders
ARTICLE_EXCLUDES = [
    'static'
]

# TEMPLATE_PAGES = {'src/books.html': 'dest/books.html',}


# Show the various article categories on the Nav menu?
DISPLAY_CATEGORIES_ON_MENU = False

TEMPLATE_PAGES = {

}

# Don't bother generating an Author page - we've only got one author
AUTHOR_SAVE_AS = ''