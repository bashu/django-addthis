from django.template import Context
from django.template import Template
from django.template import TemplateSyntaxError
from django.template import engines
from django.test import TestCase

import pytest

from addthis import settings


def template(html):
    return engines["django"].from_string(html)


class AddThisWidgetDefaultTest(TestCase):
    def setUp(self):
        self.old_ADDTHIS_SETTINGS = getattr(settings, "ADDTHIS_SETTINGS", {})
        settings.ADDTHIS_SETTINGS = {}

    def tearDown(self):
        settings.ADDTHIS_SETTINGS = self.old_ADDTHIS_SETTINGS

    def test_default(self):
        html = """{% load addthis %}{% addthis_widget "11-1234567890" %}"""
        assert "addthis_widget.js#pubid=11-1234567890" in template(html).render()

    def test_no_params(self):
        def render(t):
            return Template(t).render(Context())

        with pytest.raises(TemplateSyntaxError):
            render("""{% load addthis %}{% addthis_widget %}""")


class AddThisWidgetConfiguredTest(TestCase):
    def setUp(self):
        self.old_ADDTHIS_SETTINGS = getattr(settings, "ADDTHIS_SETTINGS", {})
        settings.ADDTHIS_SETTINGS = {"PUB_ID": "11-1234567890"}

    def tearDown(self):
        settings.ADDTHIS_SETTINGS = self.old_ADDTHIS_SETTINGS

    def test_configured(self):
        html = """{% load addthis %}{% addthis_widget %}"""
        assert "addthis_widget.js#pubid=11-1234567890" in template(html).render()
