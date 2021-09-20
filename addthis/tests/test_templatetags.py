from django.test import TestCase
from django.template import Context, Template, TemplateSyntaxError
from django.test.utils import override_settings

from addthis import settings


def template(html):
    from django.template import engines

    return engines["django"].from_string(html)

class AddThisWidgetDefaultTest(TestCase):

    def setUp(self):
       self.old_ADDTHIS_SETTINGS = getattr(settings, "ADDTHIS_SETTINGS", {})
       settings.ADDTHIS_SETTINGS = {}

    def tearDown(self):
       settings.ADDTHIS_SETTINGS = self.old_ADDTHIS_SETTINGS

    def test_default(self):
        html = """{% load addthis %}{% addthis_widget "11-1234567890" %}"""
        self.assertTrue("addthis_widget.js#pubid=11-1234567890" in template(html).render())

    def test_no_params(self):
        render = lambda t: Template(t).render(Context())
        self.assertRaises(
            TemplateSyntaxError,
            render,
            """{% load addthis %}{% addthis_widget %}""",
        )

class AddThisWidgetConfiguredTest(TestCase):

    def setUp(self):
       self.old_ADDTHIS_SETTINGS = getattr(settings, "ADDTHIS_SETTINGS", {})
       settings.ADDTHIS_SETTINGS = {"PUB_ID": "11-1234567890"}

    def tearDown(self):
       settings.ADDTHIS_SETTINGS = self.old_ADDTHIS_SETTINGS

    def test_configured(self):
        html = """{% load addthis %}{% addthis_widget %}"""
        self.assertTrue("addthis_widget.js#pubid=11-1234567890" in template(html).render())
