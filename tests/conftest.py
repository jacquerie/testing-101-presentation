# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest


@pytest.fixture
def baz():
    return {'baz': 'baz'}
