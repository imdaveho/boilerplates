"""
Django settings for {{ project_name }} project.

Include all application specifc configuration here.
"""
import os
from {{ project_name }}.settings.production import *

ALLOWED_HOSTS = ["*",]
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

PROJECT_APPS = [
    'mainapp',
]
INSTALLED_APPS += PROJECT_APPS

PROJECT_MIDDLEWARE = [
]
MIDDLEWARE_CLASSES += PROJECT_MIDDLEWARE

ADMINS = [
   ('Dave Ho', 'dave@anvilanalytics.com'),
]

MANAGERS = ADMINS + [
]

# Application Database Settings:
# import dj_database_url
# DATABASES = {
#     "default": dj_database_url.config(default="postgresql://"),
# }
# # Default Django DB Config (SQLite3)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
	"NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# See https://github.com/etianen/django-herokuapp/blob/master/

# Namespace for cache keys, if using a process-shared cache.

CACHE_MIDDLEWARE_KEY_PREFIX = "{{ project_name }}"
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # Long cache timeout for staticfiles, since this is used heavily by the optimizing storage.
    "static": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 60 * 24 * 365,
        "LOCATION": "static",
    },
}

# Logging configuration.

LOGGING = {
    "version": 1,
    # Don't throw away default loggers.
    "disable_existing_loggers": False,
    "handlers": {
        # Redefine console logger to run in production.
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        # Redefine django logger to use redefined console logging.
        "django": {
            "handlers": ["console"],
        }
    }
}

# Other Configurations:

# DEBUG_TOOLBAR_PATCH_SETTINGS = False
# SITE_ID = 1

