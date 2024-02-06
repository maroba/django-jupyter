import os.path
import shutil
import tempfile
from os.path import basename
from pathlib import Path

from bs4 import BeautifulSoup
from django.db import models
from jupyter_book.sphinx import build_sphinx


class JupyterNotebookField(models.FileField):
    description = "A serialized version of a HTML Jupyter notebook representation."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._upload_to = kwargs.get("upload_to", "")

        self.upload_to = self.upload_path

    def upload_path(self, instance, filename):
        if filename.lower().endswith(".ipynb"):
            subdir = filename.replace(".ipynb", "")
        else:
            raise ValueError(f"Invalid notebook file format: {filename}")
        return os.path.join(self._upload_to, subdir, filename)

    def pre_save(self, model_instance, add):
        file = super().pre_save(model_instance, add)

        file_path = file.path

        file_path_dir = Path(file_path).parent.absolute().resolve()

        tempdir = tempfile.mkdtemp()

        if file_path.endswith(".ipynb"):
            nb_execution_mode = "off"
            file_name = basename(file_path).replace(".ipynb", "")
        else:
            raise ValueError("Unknown file type.")

        shutil.copy(file_path, tempdir)

        sourcedir = Path(tempdir).absolute().resolve()
        outputdir = sourcedir / "_build" / "_page" / "_page" / file_name / "html"

        build_sphinx(
            sourcedir,
            outputdir,
            confoverrides={
                "latex_individualpages": True,
                "master_doc": file_name,
                "nb_execution_mode": nb_execution_mode,
            },
            use_external_toc=False,
            noconfig=True,
        )

        with open(outputdir / f"{file_name}.html", "r") as fh:
            html_doc = fh.read()

        soup = BeautifulSoup(html_doc, "html.parser")
        article = soup.find("article")
        imgs = article.find_all("img")
        for img in imgs:
            if img["src"].startswith("_images/"):
                img["src"] = img["src"].replace("_images", "{{ notebook_dir }}/_images")
        article_html = str(article)

        with open(outputdir / "article.html", "w") as fh:
            fh.write(article_html)

        shutil.copy(outputdir / "article.html", file_path_dir)
        if os.path.exists(outputdir / "_images"):
            shutil.copytree(outputdir / "_images", file_path_dir / "_images")

        shutil.rmtree(tempdir)

        return file
