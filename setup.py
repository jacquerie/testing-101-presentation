# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from setuptools import setup


setup(
    name='foobar',
    version='0.0.1',
    packages=[
        'foobar',
    ],
    install_requires=[
        'httpretty',
        'mock',
        'pytest',
        'pytest-httpretty',
        'requests',
    ],
)
