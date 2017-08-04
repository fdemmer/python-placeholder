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


def draw_cross(drawing, fill='silver', width=1):
    size = drawing.im.size
    drawing.line((0, 0) + size, fill, width)
    drawing.line((0, size[1], size[0], 0), fill, width)


def draw_circle(drawing, fill=None, outline='darkgray'):
    size = drawing.im.size
    # diameter should be the size of the shorter dimension
    d = min(size)
    # calculate center position
    left, top = (x / 2 for x in map(sub, drawing.im.size, (d, d)))
    right, bottom = left + d, top + d
    drawing.ellipse((left, top, right, bottom), fill, outline)
