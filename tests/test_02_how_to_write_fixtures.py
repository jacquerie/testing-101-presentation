# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os
import pkg_resources

import pytest


#
# Fixtures
#

@pytest.fixture
def foo():
    return {'foo': 'foo'}


@pytest.fixture
def bar():
    return {'bar': 'bar'}


def test_02_01_fixtures_avoid_repeating_code(foo, bar):
    assert foo == bar


#
# Fixtures From The Filesystem
#

@pytest.fixture
def foobar():
    return pkg_resources.resource_string(
        __name__, os.path.join('fixtures', 'foobar'))


def test_02_02_fixtures_can_be_fetched_from_the_filesystem(foobar):
    assert foobar == 'baz'


#
# Fixtures As Control Flow
#

@pytest.fixture
def junk():
    with open('junk', 'w') as f:
        f.write('junk')

    yield

    os.remove('junk')


def test_02_03_fixtures_can_be_used_to_control_flow(junk):
    expected = 'junk'
    with open('junk', 'r') as f:
        result = f.read()

    assert expected == result


#
# Fixtures From Conftest.py
#

def test_02_04_fixtures_can_be_retrieved_from_the_conftest(baz):
    assert {'baz': 'baz'} == baz
