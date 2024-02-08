import os

import django


BASE_DIR = os.path.dirname(__file__)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

INSTALLED_APPS = (
    "tests",
    "django_jupyter",
)


MIDDLEWARE_CLASSES = []

SECRET_KEY = "123"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
