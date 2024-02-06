from pathlib import Path

from django.conf import settings
from django.template import Library, Template, Context
import os

register = Library()


@register.inclusion_tag("django_jupyter/header.html")
def jupyter_header():
    pass


@register.inclusion_tag("django_jupyter/article.html")
def jupyter_notebook(notebook):
    notebook_dir = Path(notebook.path).parent.absolute().resolve()

    with open(notebook_dir / "article.html", "r") as fh:
        article_template = fh.read()

    notebook_dir = str(notebook_dir).replace(str(settings.MEDIA_ROOT), "")[1:]
    notebook_dir = os.path.join(settings.MEDIA_URL, notebook_dir)
    template = Template(article_template)
    content = template.render(Context({"notebook_dir": str(notebook_dir)}))
    return {"content": content}


@register.inclusion_tag("django_jupyter/after_body.html")
def jupyter_after_body():
    pass
