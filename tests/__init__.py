import os
import tempfile
from unittest import TestCase

from PIL import Image

from placeholder import PlaceHolderImage


class PlaceHolderImageTests(TestCase):
    def setUp(self):
        self.filename = tempfile.mktemp()

    def tearDown(self):
        if os.path.exists(self.filename):
            os.unlink(self.filename)

    def test_create(self):
        placeholder = PlaceHolderImage(200, 100)
        placeholder.save_image(self.filename)

    def test_dimensions(self):
        placeholder = PlaceHolderImage(200, 100)
        placeholder.save_image(self.filename)

        imagefile = Image.open(self.filename)
        self.assertEqual(imagefile.size, (200, 100))

    def test_odd_dimensions(self):
        placeholder = PlaceHolderImage(1, 1)
        placeholder.save_image(self.filename)

        imagefile = Image.open(self.filename)
        self.assertEqual(imagefile.size, (1, 1))

        placeholder = PlaceHolderImage(201, 199)
        placeholder.save_image(self.filename)

        imagefile = Image.open(self.filename)
        self.assertEqual(imagefile.size, (201, 199))
