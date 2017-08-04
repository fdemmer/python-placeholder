*Simple module for creating placeholder images*


install by

::

    $ pip install python-placeholder


Example:
=========

.. code:: python

    from placeholder import PlaceHolderImage

    placeholder = PlaceHolderImage(width=300, height=200)

    # get PIL.Image instance
    image = placeholder.get_image()

    # write to a file as png
    placeholder.save('placeholder.png')

    # write in jpeg encoding
    placeholder.save('placeholder.jpg')

    # alternatively initialize with empty or custom text
    PlaceHolderImage(300, 200, text='')

    # colors can be set using names or hex-tuples incl transparency
    PlaceHolderImage(300, 200, fg_color=(0, 0, 0, 0), bg_color='red')


Known bugs:
============

- if you do not provide absolute path to font to PlaceHolderImage the default font used will have very small size.

- if you get something like The _imagingft C module is not installed, look here https://stackoverflow.com/questions/4011705/python-the-imagingft-c-module-is-not-installed

Run tests:
==========

You can run the testsuite with the following command::

    python -m unittest tests

Or use tox_ to test against all supported python versions.

.. _tox: https://testrun.org/tox/latest/
