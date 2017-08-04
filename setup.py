from setuptools import setup, find_packages


setup(
    name='python-placeholder',
    version='0.2+fdemmer.1',
    description='Placeholder is a simple little python module that creates (drumroll..) placeholder images, based on work of Martin Marcher',
    author="Florian Demmer",
    url='https://github.com/fdemmer/python-placeholder',
    packages=['placeholder'],
    include_package_data=True,
    install_requires=[
        'pillow',
    ],

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='placeholder,images',
)
