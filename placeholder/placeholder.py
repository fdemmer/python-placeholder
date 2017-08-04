# -*- coding: utf-8 -*-
from operator import sub

__docformat__ = u'restructuredtext en'

from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps

get_color = lambda name: ImageColor.getrgb(name)


def get_font(name, size, encoding):
    try:
        return ImageFont.truetype(name, size=size, encoding=encoding)
    except IOError:
        return ImageFont.load_default()


class PlaceHolderImage(object):
    def __init__(self, width, height, fg_color=get_color('black'),
            bg_color=get_color('grey'), text=None, font=u'Verdana.ttf',
            fontsize=42, encoding='', mode='RGBA'):
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
        self.width = width
        self.height = height
        self.size = width, height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.mode = mode

        self.font = get_font(font, fontsize, encoding)

        if text is None:
            self.text = '{}x{}'.format(width, height)
        else:
            self.text = text

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
        result_img = Image.new(self.mode, self.size, self.bg_color)

        text_img = Image.new("RGBA", self.size, self.bg_color)

        # calculate center position for the text
        left, top = (x / 2 for x in map(sub, self.size, self.font.getsize(self.text)))

        drawing = ImageDraw.Draw(text_img)
        drawing.text((left, top),
                     self.text,
                     font=self.font,
                     fill=self.fg_color)

        txt_img = ImageOps.fit(text_img, self.size, method=Image.BICUBIC, centering=(0.5, 0.5))

        result_img.paste(txt_img)
        txt_img.save(fp, format, **params)
