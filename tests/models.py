import django.db.models as models
from django_jupyter.models import JupyterNotebookField


class SampleModel(models.Model):
    notebook = JupyterNotebookField()
