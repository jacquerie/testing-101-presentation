# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from .bar import bar


def foo():
    return 'foo: {bar}'.format(bar=bar())


def foo2():
    return 'foo2: {foo}'.format(foo=foo())
