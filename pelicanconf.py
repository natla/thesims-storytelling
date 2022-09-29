from markdown import Markdown
markdown = Markdown(extensions=['markdown.extensions.extra'])

def md(content, *args):
    return markdown.convert(content)

JINJA_FILTERS = {
    'md': md,
}

AUTHOR = 'natla'
SITENAME = 'Symphony Garden'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)
#
# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
LINKS = []
SOCIAL = []

DEFAULT_PAGINATION = 2

DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

ARTICLE_PATHS = ['posts']

OUTPUT_PATH = 'docs/'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DIRECT_TEMPLATES = ['archives']
TEMPLATE_EXTENSIONS = ['.html']
TEMPLATE_PAGES = {
    'theme/templates/index.html': 'index.html',
    'theme/templates/bios.html': 'bios.html',
    'theme/templates/contact.html': 'author.html',
    # 'theme/templates/pagination.html': 'page.html',
}
THEME_TEMPLATES_OVERRIDES = ['content/theme/templates']
THEME = 'content/theme'

STATIC_PATHS = ['theme/static']

TAG_SAVE_AS = '{slug}.html'
TAG_URL = '{slug}.html'
