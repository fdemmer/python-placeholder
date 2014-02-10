#!/usr/bin/python
# -*- coding: utf-8 -*-

# placeholder.py --- short description
#
# Copyright  (C)  2010  Martin Marcher <martin@marcher.name>
#
# Version:
# Keywords:
# Author: Martin Marcher <martin@marcher.name>
# Maintainer: Martin Marcher <martin@marcher.name>
# URL: http://
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
__docformat__ = u'restructuredtext en'


import os
import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageFont
from PIL import ImageOps



get_color = lambda name: ImageColor.getrgb(name)

class PlaceHolderImage:
    """Create an image useable for wireframing websites.
    """

    def __init__(self, width, height,
                 fg_color=Color.BLACK,
                 bg_color=Color.WHITE,
                 text=None,
                 font=u'Verdana.ttf',
                 fontsize=24,
                 encoding=u'unic',
                 mode=Color.MODE,
                 fmt=u'PNG'):

        self._width = width
        self._height = height
        self._bg_color = bg_color
        self._fg_color = fg_color
        self._text = text
        self._font = font
        self._fontsize = fontsize
        self._encoding = encoding

        self._size = Size(self._width, self._height)
        self._mode = mode
        self._fmt = fmt

    def save(self):

        from tempfile import NamedTemporaryFile
        with NamedTemporaryFile(delete=False) as target:
            result_img = Image.new(self._mode, self._size, self._bg_color)
            img_width, img_height = result_img.size

            self.log.debug(u'result_img.size: %r, self._size: %r',
                           result_img.size, self._size)

            if self._text is None:
                self._text = "x".join([str(n) for n in self._size])
            if self._text is not None:
                try:
                    font = ImageFont.truetype(
                        self._font,
                        size=self._fontsize,
                        encoding=self._encoding)
                except (IOError, ) as error:
                    font = ImageFont.load_default()

                self.log.debug(u'The text is: %r', self._text)
                txt_size = Size(*font.getsize(self._text))
                self.log.debug(u'Text Size: %r', txt_size)
                txt_img = Image.new("RGBA", self._size, self._bg_color)
                self.log.debug(u'Size of txt_img: %r', txt_size)

                drawing = ImageDraw.Draw(txt_img)
                left = self._size.width / 2 - txt_size.width / 2
                top = self._size.height / 2 - txt_size.height / 2
                drawing.text((left, top, ),
                             self._text,
                             font=font,
                             fill=self._fg_color)

                txt_img = ImageOps.fit(txt_img,
                                       result_img.size,
                                       method=Image.BICUBIC,
                                       centering=(0.5, 0.5)
                                       )
                result_img.paste(txt_img)
            # result_img.show()
            # sys.exit(1)
            txt_img.save(target, self._fmt)
            self.log.debug(u'Wrote Image to: %r', target.name)
            del(result_img)
        return target.name




