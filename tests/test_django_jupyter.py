import glob
import os
import os.path
import shutil
from pathlib import Path

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from tests.models import SampleModel

BASE_DIR = Path(os.path.abspath(os.path.join(os.path.dirname(__file__))))


class TestSmoke(TestCase):

    def setUp(self):
        shutil.rmtree(BASE_DIR / "media" / "example", ignore_errors=True)

    def tearDown(self):
        shutil.rmtree(BASE_DIR / "media" / "example", ignore_errors=True)

    def create_instance(self):
        filename = Path(os.path.dirname(__file__)) / "fixtures" / "example.ipynb"
        with open(filename, "rb") as file_:
            django_file = file_.read()

        instance = SampleModel()
        instance.notebook = SimpleUploadedFile("example.ipynb", django_file)
        instance.save()
        return instance

    def assert_media_files_exists(self):
        self.assertTrue(os.path.exists(BASE_DIR / "media" / "example"))
        self.assertTrue(os.path.exists(BASE_DIR / "media" / "example" / "article.html"))
        self.assertTrue(os.path.exists(BASE_DIR / "media" / "example" / "_images"))
        pattern = os.path.join(BASE_DIR / "media" / "example", "**/*.png")
        png_files = glob.glob(pattern, recursive=True)
        self.assertTrue(len(png_files) == 1)

    def assert_media_files_do_not_exists(self):
        self.assertFalse(os.path.exists(BASE_DIR / "media" / "example"))

    def test_happy_path(self):
        # Start with empty media directory
        self.assert_media_files_do_not_exists()

        # Saving an instance should create media files
        instance = self.create_instance()
        self.assert_media_files_exists()

        # Deleting the instance should tidy up the media files
        instance.delete()

        self.assert_media_files_do_not_exists()
