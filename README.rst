Simple class to create placeholder images for wireframing.


Example:
=========

::

        # Shows the default values used
        # If text is None the image size will be used as text
        from placeholder import PlaceHolderImage, Color
        img = PlaceHolderImage(width, height,
                                fg_color=Color.BLACK,
                                bg_color=Color.WHITE,
                                text=None,
                                font=u'Verdana.ttf',
                                fontsize=24,
                                encoding=u'unic',
                                mode=Color.MODE,
                                fmt=u'PNG')
        result_path = img.save()

        # Somewhat less to type
        # bg is white
        # fg is black
        img = PlaceHolderImage(width, height)
        result_path = img.save()

