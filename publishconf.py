# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

from pelicanconf import *  # pylint: disable=wildcard-import

sys.path.append(os.curdir)

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://symphony-garden.cf'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

#GOOGLE_ANALYTICS = ""
