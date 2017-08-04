# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from operator import sub

from PIL import Image, ImageDraw, ImageFont


def get_font(name, size, encoding):
    try:
        return ImageFont.truetype(name, size=size, encoding=encoding)
    except IOError:
        return ImageFont.load_default()


class PlaceHolderImage(object):
    def __init__(self, width, height, fg_color='darkgrey', bg_color='lightgrey',
            text=None, font='arial', fontsize=36, encoding='',
            mode='RGBA'):
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

        self.size = width, height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.mode = mode

        self.font = get_font(font, fontsize, encoding)

        if text is None:
            self.text = '{}x{}'.format(width, height)
        else:
            self.text = text

    def draw_text(self, text, fill=None, font=None):
        assert self._image, 'get_image() must be called before drawing text'
        fill = self.fg_color if fill is None else fill
        font = self.font if font is None else font

        # calculate center position for the text
        left, top = (x / 2 for x in map(sub, self.size, font.getsize(text)))

        drawing = ImageDraw.Draw(self._image)
        drawing.text((left, top), text, font=font, fill=fill)

    def get_image(self):
        """
        Generate the image and return it.

        :return: the image as a PIL.Image instance
        """
        self._image = Image.new(self.mode, self.size, self.bg_color)
        if self.text:
            self.draw_text(self.text, fill=self.fg_color, font=self.font)
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
