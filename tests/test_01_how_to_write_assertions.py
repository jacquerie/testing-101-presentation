# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest


#
# Basic Stuff
#

def test_01_01_pytest_dash_k_can_be_used_to_select_tests():
    assert True


def test_01_02_pytest_overloads_assert():
    assert 'foo' == 'bar'


def test_01_03_assertions_can_be_pythonic():
    assert 'foo' in ['bar', 'baz']


def test_01_04_assertions_can_have_extra_messages():
    assert 'foo' in ['bar', 'baz'], 'foo is not there'


#
# Exceptions And Failures
#

class FooException(RuntimeError):
    pass


def raise_foo_exception(msg=''):
    raise FooException(msg)


def test_01_05_pytest_can_assert_that_exceptions_have_happened():
    with pytest.raises(FooException):
        raise_foo_exception()


def test_01_06_pytest_can_assert_that_their_error_messages_were_good():
    with pytest.raises(FooException) as excinfo:
        raise_foo_exception('foo')
    assert 'foo' in str(excinfo.value)


@pytest.mark.xfail
def test_01_07_pytest_can_mark_a_test_as_an_expected_failure():
    raise_foo_exception()


#
# Better Assertions
#

def test_01_08_keyerror_hides_assertion_errors():
    foo = {'foo': 'foo'}
    bar = {'bar': 'bar'}

    assert foo['baz'] == bar['baz']


def test_01_09_using_get_is_not_a_solution():
    foo = {'foo': 'foo'}
    bar = {'bar': 'bar'}

    assert foo.get('baz') == bar.get('baz')


def test_01_10_removing_logic_from_assertions_is_better():
    foo = {'foo': 'foo'}
    bar = {'bar': 'bar'}

    expected = 'baz'
    result = foo.get('baz')

    assert expected == result

    expected = 'baz'
    result = bar.get('baz')

    assert expected == result


def test_01_11_directly_comparing_objects_is_also_nice():
    foo = {'foo': 'foo'}
    bar = {'bar': 'bar'}

    assert foo == bar
