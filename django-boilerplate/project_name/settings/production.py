import sys
from {{ project_name }}.settings.default import *

# Custom Project Structure:

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, BASE_DIR)
sys.path.insert(1, APPS_DIR)
sys.path.insert(2, os.path.join(BASE_DIR, 'libs'))

# Production Configs (overwriting base.py):

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ROOT_PATH = os.path.dirname(__file__)
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
PREPEND_WWW = False
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_STORAGE = "django.contrib.sessions.backends.signed_cookies"
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Template Stuff (overwriting base.py):

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(ROOT_PATH, 'templates'),
)

TEMPLATE_LOADERS = (
    ("django.template.loaders.cached.loader", (
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    )),
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    # "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
]

# Miscellaneous:

TEST_RUNNER = "django.test.runner.DiscoverRunner"
