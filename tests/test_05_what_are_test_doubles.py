# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from requests import Response

from foobar.fetch import fetch_with_dependency_injection


#
# Dummies
#

class DummyLib(object):
    pass


def test_05_01_dummies_can_be_used_to_satisfy_the_api_of_a_method():
    dummy_lib = DummyLib()

    response = fetch_with_dependency_injection(dummy_lib, 'http://example.com')

    assert response.status_code == 200
    assert 'Example Domain' in response.content


#
# Stubs
#

class StubLib(object):
    def get(self, url):
        response = Response()
        response.status_code = 200
        response._content = 'Stub Domain'

        return response


def test_05_02_stubs_are_pre_programmed_implementations_of_the_method():
    stub_lib = StubLib()

    response = fetch_with_dependency_injection(stub_lib, 'http://example.com')

    assert response.status_code == 200
    assert 'Stub Domain' in response.content


#
# Fakes
#

class FakeLib(object):
    def __init__(self):
        self.responses = {}

    def _add(self, url, response):
        self.responses[url] = response

    def get(self, url):
        return self.responses[url]


class StubResponse(object):
    content = 'Fake Domain'
    status_code = 200


def test_05_03_fakes_are_toy_implementations_of_the_method():
    fake_lib = FakeLib()
    fake_lib._add('http://example.com', StubResponse())

    response = fetch_with_dependency_injection(fake_lib, 'http://example.com')

    assert response.status_code == 200
    assert 'Fake Domain' in response.content
