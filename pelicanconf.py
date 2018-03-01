#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wesley Klock'
SITENAME = "Melon's Band"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

THEME = './pelican-themes/attila'

HEADER_COVER= 'images/home-bg.jpg'
HOME_LOGO = 'images/music-logo.png'

#SITE_LOGO = 'images/logo.png'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#CSS_OVERWRITE = './pelican-themes/chameleon/static/css/bootstrap.css'

STATIC_PATHS = [
    'images',
    'extra/icon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/icon.ico': {'path': 'favicon.ico'}
}


MENUITEMS = [
    ('Home', '/'),
    ('Archives', [
        ('Tags', '/tags.html'),
        ('Categories', '/categories.html'),
        ('Chronological', '/archives.html'),
        ]),
    ('Social', [
        ('Email', 'mailto: maurelinus@stoic.edu'),
        ('Github', 'http://url-to-github-page'),
        ('Facebook', 'http://url-to-facebook-page'),
        ]),
    ]

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

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

### Plugins

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# Analytics

### Theme specific settings


AUTHORS_BIO = {
  "Wesley Klock": {
    "name": "Wesley Klock",
    "cover": "images/Wesley.png",
    "image": "images/Wesley.png",
    "website": "http://blog.arulraj.net",
    "location": "Austin, Texas",
    "bio": "I kind of like applesauce more than apples. It may just be the sugar tho."
  }
}
