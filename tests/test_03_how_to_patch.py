# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest
from mock import patch

from foobar.foo import foo, foo2


#
# Patching
#

@patch('foobar.foo.bar')
def test_03_01_patch_replaces_method_calls(mock_bar):
    bar.return_value = 'bar: mock baz'

    expected = 'foo: bar: baz'
    result = foo()

    assert expected == result


@patch('foobar.foo.bar')
def test_03_02_patch_works_on_uses_not_definitions(mock_bar):
    bar.return_value = 'bar: mock baz'

    expected = 'foo: bar: mock baz'
    result = foo()

    assert expected == result


@patch('foobar.foo.bar', return_value='bar: mock baz')
def test_03_03_patch_supports_an_abbreviated_syntax(mock_bar):
    expected = 'foo: bar: mock baz'
    result = foo()

    assert expected == result


#
# Side Effects
#

@patch('foobar.foo.bar', side_effect=RuntimeError)
def test_03_04_patch_can_be_used_to_raise_exceptions(mock_bar):
    with pytest.raises(RuntimeError):
        foo()


@patch('foobar.foo.bar', side_effect=['bar: mock bar', 'bar: mock baz'])
def test_03_05_patch_can_be_used_to_return_multiple_values(mock_bar):
    expected = 'foo: bar: mock bar'
    result = foo()

    assert expected == result

    expected = 'foo: bar: mock baz'
    result = foo()

    assert expected == result


#
# Gotchas
#

@patch('foobar.foo.foo')
@patch('foobar.foo.bar')
def test_03_06_watch_out_for_the_order_of_patches(mock_foo, mock_bar):
    mock_foo.return_value = 'foo: mock foo'
    mock_bar.return_value = 'bar: mock bar'

    expected = 'foo2: foo: mock foo'
    result = foo2()

    assert expected == result


@patch('foobar.foo.foo')
@patch('foobar.foo.bar')
def test_03_07_watch_out_for_mocks_shadowing_the_test_subject(foo, bar):
    foo.return_value = 'foo: mock foo'
    bar.return_value = 'bar: mock bar'

    expected = 'bar: mock bar'
    result = foo()

    assert expected == result
