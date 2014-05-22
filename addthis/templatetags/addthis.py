from __future__ import absolute_import

from django import template

from addthis import settings

register = template.Library()


@register.inclusion_tag('addthis/widget_js.html')
def addthis_widget(pub_id=None):
    from django.template import TemplateSyntaxError

    if pub_id is None:
        addthis = getattr(settings, 'ADDTHIS_SETTINGS')
        if 'PUB_ID' in addthis:
            pub_id = addthis['PUB_ID']
        else:
            raise TemplateSyntaxError('The `addthis_widget` template tag requires a `pub_id`. You must either pass it as an argument or set ADDTHIS_SETTINGS[\'PUB_ID\'] in your settings.')

    return {
        'pub_id': pub_id,
    }


# See: http://github.com/lettertwo/django-socialsharing
@register.inclusion_tag('addthis/config_js.html')
def addthis_config():
    return {
        'addthis': settings.ADDTHIS_SETTINGS,
    }
