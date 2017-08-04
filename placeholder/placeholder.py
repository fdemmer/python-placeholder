# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial

from PIL import Image, ImageDraw, ImageFont

from placeholder.draw import draw_text


def get_font(name, size, encoding):
    try:
        return ImageFont.truetype(name, size=size, encoding=encoding)
    except IOError:
        return ImageFont.load_default()


class PlaceHolderImage(object):
    def __init__(self, width, height, fg_color='darkgrey', bg_color='gainsboro',
            text=None, font='arial', fontsize=36, encoding='',
            mode='RGBA', draw=None):
        """
        Create an image usable for wireframing websites.

        :param width: image width in pixels
        :param height: image height in pixels
        :param fg_color: foreground color as RGB tuple
        :param bg_color: background color as RGB tuple
        :param text: text to write in the center of the image
            (default: None, to write the image dimensions)
        :param font: TrueType font
        :param fontsize: font size, in points (only used when font is available)
        :param encoding: font encoding
            (used with ImageFont.truetype, which defaults to Unicode)
        :param mode: color mode
            (default: 'RGBA', see Pillow documentation for valid modes:
            http://pillow.readthedocs.io/en/latest/handbook/concepts.html#modes)
        """
        self._image = None
        self._draw_functions = []

        assert width > 0, 'width must be > 0'
        assert height > 0, 'height must be > 0'

        self.size = width, height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.mode = mode

        # append more drawing functions
        for func in draw or []:
            self._draw_functions.append(func)

        # text will be drawn last/on top
        if text is None:
            text = '{}x{}'.format(width, height)
        if text:
            self._draw_functions.append(
                partial(
                    draw_text, text=text, fill=self.fg_color,
                    font=get_font(font, fontsize, encoding),
                )
            )

    def _draw_everything(self):
        """
        Call all the registered draw functions.
        """
        drawing = ImageDraw.Draw(self._image)
        for func in self._draw_functions:
            func(drawing)

    def get_image(self):
        """
        Generate the image and return it.

        :return: the image as a PIL.Image instance
        """
        self._image = Image.new(self.mode, self.size, self.bg_color)
        self._draw_everything()
        return self._image

    def save(self, fp, format=None, **params):
        """
        Save the image to the given filename.

        This generates the image if necessary and calls PIL.Image.save().

        :param fp: A filename (string), pathlib.Path object or file object.
        :param format: Optional format override.  If omitted, the
           format to use is determined from the filename extension.
           If a file object was used instead of a filename, this
           parameter should always be used.
       :param params: Extra parameters to the image writer.
        """
        if not self._image:
            self.get_image()
        self._image.save(fp, format, **params)
