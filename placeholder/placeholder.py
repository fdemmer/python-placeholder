# -*- coding: utf-8 -*-
__docformat__ = u'restructuredtext en'

from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps

get_color = lambda name: ImageColor.getrgb(name)


class PlaceHolderImage(object):
    """Create an image usable for wireframing websites."""
    def __init__(self, width, height, fg_color=get_color('black'),
            bg_color=get_color('grey'), text=None, font=u'Verdana.ttf',
            fontsize=42, encoding='', mode='RGBA'):

        self.width = width
        self.height = height
        self.size = width, height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text = text if text else '{0}x{1}'.format(width, height)
        self.font = font
        self.fontsize = fontsize
        self.encoding = encoding
        self.mode = mode

    def save(self, fp, format=None, **params):
        """
        Save the image to the given filename.

        This generates the image and calls PIL.Image.save().

        :param fp: A filename (string), pathlib.Path object or file object.
        :param format: Optional format override.  If omitted, the
           format to use is determined from the filename extension.
           If a file object was used instead of a filename, this
           parameter should always be used.
       :param params: Extra parameters to the image writer.
        """
        try:
            font = ImageFont.truetype(self.font, size=self.fontsize, encoding=self.encoding)
        except IOError:
            font = ImageFont.load_default()

        result_img = Image.new(self.mode, self.size, self.bg_color)

        text_size = font.getsize(self.text)
        text_img = Image.new("RGBA", self.size, self.bg_color)

        # position for the text
        left = self.size[0] / 2 - text_size[0] / 2
        top = self.size[1] / 2 - text_size[1] / 2

        drawing = ImageDraw.Draw(text_img)
        drawing.text((left, top),
                     self.text,
                     font=font,
                     fill=self.fg_color)

        txt_img = ImageOps.fit(text_img, self.size, method=Image.BICUBIC, centering=(0.5, 0.5))

        result_img.paste(txt_img)
        txt_img.save(fp, format, **params)
