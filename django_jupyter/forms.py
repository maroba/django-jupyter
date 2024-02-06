import os

from django import forms
from django.core.exceptions import ValidationError


class JupyterNotebookField(forms.FileField):

    def clean(self, value, initial=None):
        value = super().clean(value, initial)

        filename = value.name
        _, extension = os.path.splitext(filename)
        if extension.lower() != ".ipynb":
            raise ValidationError("Only .ipynb files are allowed.")

        return value
