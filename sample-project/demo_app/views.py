from django.views.generic import CreateView, TemplateView

from .models import MyModel
from .forms import MyModelForm


class MyModelFormView(CreateView):
    model = MyModel
    form_class = MyModelForm
    template_name = "form-view.html"

    success_url = "/test2/"


class NotebookView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        instance = MyModel.objects.last()
        ctx["notebook"] = instance.notebook
        return ctx
