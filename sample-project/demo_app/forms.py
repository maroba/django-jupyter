from django.forms import ModelForm

from django_jupyter.forms import JupyterNotebookField
from .models import MyModel


class MyModelForm(ModelForm):

    class Meta:
        model = MyModel
        fields = "__all__"

    notebook = JupyterNotebookField()
