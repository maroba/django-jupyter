from django.db import models

from django_jupyter.models import JupyterNotebookField


class MyModel(models.Model):
    notebook = JupyterNotebookField(upload_to="notebooks")
