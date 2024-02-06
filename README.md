# django-jupyter

A Django app for storing Jupyter notebooks in your database and rendering them in views.

## Installation

First install the package:

```
pip install -U django-jupyter
```

Then activate the app in our `settings.py`:

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    ...
    "django_jupyter",
    ...
]
```
