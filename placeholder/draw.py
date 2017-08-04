# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import sub


def draw_text(drawing, text, fill=None, font=None):
    """
    Drawing function to draw centered text.

    :param drawing: ImageDraw instance, all drawing functions must accept that
        as their first argument
    :param text: text to draw, a string
    :param fill: fill color
    :param font: ImageFont instance
    """
    # calculate center position
    left, top = (x / 2 for x in map(sub, drawing.im.size, font.getsize(text)))
    drawing.text((left, top), text, font=font, fill=fill)
