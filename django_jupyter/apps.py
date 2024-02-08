import shutil
from pathlib import Path

from django.apps import AppConfig
from django.db.models.signals import post_delete

from django_jupyter.models import JupyterNotebookField


def post_delete_handler(sender, **kwargs):
    """Tidy up files after model instance has been deleted."""

    instance = kwargs["instance"]

    for field in instance._meta.fields:
        # TODO: we should cache which models hold notebook fields
        if isinstance(field, JupyterNotebookField):
            path = Path(getattr(instance, field.name).path).parent
            shutil.rmtree(path)


class DjangoJupyterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_jupyter"

    def ready(self):
        post_delete.connect(post_delete_handler)
