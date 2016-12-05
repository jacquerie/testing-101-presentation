# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os
import pkg_resources

import httpretty
import pytest
from mock import patch
from requests import Response

from foobar.fetch import fetch


#
# Patching Is Not Always The Best Solution
#

@pytest.fixture
def content():
    return pkg_resources.resource_string(
        __name__, os.path.join('fixtures', 'example.com.html'))


@patch('foobar.fetch.requests.get')
def test_04_01_you_can_patch_methods_that_do_http_requests(get, content):
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = content

    get.return_value = mock_response

    response = fetch('http://example.com')

    assert response.status_code == 200
    assert 'Hello, world!' in response.content


#
# For HTTP Requests, HTTPretty Is Better
#

@pytest.fixture
def httpretty_fixture():
    httpretty.enable()
    yield
    httpretty.disable()


def test_04_02_but_you_should_use_httpretty(httpretty_fixture, content):
    httpretty.register_uri(httpretty.GET, 'http://example.com', body=content)

    response = fetch('http://example.com')

    assert response.status_code == 200
    assert 'Hello, world!' in response.content


@httpretty.activate
def test_04_03_httpretty_activate_does_not_work(content):
    httpretty.register_uri(httpretty.GET, 'http://example.com', body=content)

    response = fetch('http://example.com')

    assert response.status_code == 200
    assert 'Hello, world!' in response.content


@pytest.mark.httpretty
def test_04_04_pytest_httpretty_allows_to_use_a_simpler_decorator(content):
    httpretty.register_uri(httpretty.GET, 'http://example.com', body=content)

    response = fetch('http://example.com')

    assert response.status_code == 200
    assert 'Hello, world!' in response.content


@pytest.mark.httpretty
def test_04_05_httpretty_can_return_any_status_code():
    httpretty.register_uri(httpretty.GET, 'http://example.com', status=404)

    response = fetch('http://example.com')

    assert response.status_code == 404
    assert 'Hello, world!' not in response.content
