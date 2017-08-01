#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'nogaems'
SITENAME = 'All we need a blog'
SITEURL = ''

THEME = 'pelican-bold'

PATH = 'content'
STATIC_PATHS = ['blog', 'downloads', 'media']
OUTPUT_PATH = 'docs/'

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

#SITESUBTITLES = ('Надпись слева', 'и ещё одна надпись справа')
SITESUBTITLES = ('No matter how fast I run', 'I cannot run away from the pain')
DISPLAY_PAGES_ON_MENU = True
DISQUS_SITENAME = None

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
