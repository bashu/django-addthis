from django import template
from django.template import TemplateSyntaxError

from addthis import settings

register = template.Library()


@register.inclusion_tag("addthis/widget_js.html")
def addthis_widget(pub_id=None):
    if pub_id is None:
        addthis = settings.ADDTHIS_SETTINGS
        if "PUB_ID" in addthis:
            pub_id = addthis["PUB_ID"]
        else:
            msg = (
                "The `addthis_widget` template tag requires a site profile id. "
                "Either pass it as `pub_id`, or set "
                "ADDTHIS_SETTINGS['PUB_ID'] in your settings."
            )
            raise TemplateSyntaxError(msg)

    return {
        "pub_id": pub_id,
        "addthis": settings.ADDTHIS_SETTINGS,
    }
