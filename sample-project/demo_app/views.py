from django.views.generic import CreateView, TemplateView, RedirectView

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
        instance = MyModel.objects.get(pk=self.kwargs["pk"])
        ctx["notebook"] = instance.notebook
        return ctx


class NotebookDeleteView(RedirectView):
    url = "/upload/"

    def get(self, request, *args, **kwargs):
        MyModel.objects.get(pk=self.kwargs["pk"]).delete()
        return super().get(request, *args, **kwargs)
