# django-jupyter

A Django app for storing Jupyter notebooks in your database and rendering them in views.

## Features

#### Use Jupyter notebook as a database field

```python
from django.db import models
from django_jupyter.models import JupyterNotebookField


class MyModel(models.Model):
    # ... other model fields ...
    notebook = JupyterNotebookField(upload_to="notebooks")
    # ... other model fields ...

```

This would store related media files (like images in your notebook) in a directory
tree in `MEDIA_ROOT / "notebooks"`.

#### Upload Jupyter notebook with custom form field

```python
from django import forms
from django_jupyter.forms import JupyterNotebookField


class MyForm(forms.Form):
    # ... other form fields
    notebook = JupyterNotebookField()
    # ... other form fields

```

#### Render the notebook in a view using tags

Just load the tag library, put the tags `jupyter_header` and `jupyter_after_body` at their appropriate
location and render the notebook using the `jupyter_notebook` tag:

```html
<!DOCTYPE html>

<!-- Load the tag library -->
{% load jupyter_tags %}

<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

    <!-- Load the Jupyter notebook styling -->
    {% jupyter_header %}

</head>

<body>

<div class="container mt-3" style="max-width: 840px">

    <!-- Render notebook -->
    {% jupyter_notebook notebook %}

</div>

</body>

<!-- Load Bootstrap and stuff for code highlighting. -->
{% jupyter_after_body %}

</html>
```

The `notebook` variable is pushed into the view context as usual in Django:

```python
def my_view(request):
    my_instance = MyModel.objects.first()
    return render(request, template_name, {
        "notebook": my_instance.notebook
    })
```

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
