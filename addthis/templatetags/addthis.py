from django import template


register = template.Library()


@register.inclusion_tag('addthis/widget_js.html')
def addthis_widget(pub_id=None):
    from django.conf import settings
    from django.template import TemplateSyntaxError

    if pub_id is None:
        pub_id = getattr(settings, 'ADDTHIS_PUB_ID', None)

    if pub_id is None:
        raise TemplateSyntaxError(
            'The `addthis_widget` template tag requires a `pub_id`. You must either pass it as an argument or set ADDTHIS_PUB_ID in your settings.')

    return {
        'pub_id': pub_id,
    }


# See: http://github.com/lettertwo/django-socialsharing
@register.inclusion_tag('addthis/config_js.html')
def addthis_config():
    from django.conf import settings
    from django.template import TemplateSyntaxError

    if getattr(settings, 'ADDTHIS_GA_TRACKING_ENABLED', False):
        data_ga_property = getattr(settings, 'ADDTHIS_DATA_GA_PROPERTY', getattr(
            settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', None))
        if data_ga_property is None:
            raise TemplateSyntaxError(
                'The `addthis_config` template tag is configured to use Google Analytics but a tracking code was not found. You must set ADDTHIS_DATA_GA_PROPERTY or GOOGLE_ANALYTICS_PROPERTY_ID in settings.py')
    else:
        data_ga_property = None

    twitter_bitly = getattr(settings, 'ADDTHIS_TWITTER_BITLY', False)
    twitter_via = getattr(settings, 'ADDTHIS_TWITTER_VIA', None)
    data_ga_social = getattr(settings, 'ADDTHIS_DATA_GA_SOCIAL', True)
    data_track_addressbar = getattr(settings, 'ADDTHIS_DATA_TRACK_ADDRESSBAR', True)
    data_track_clickback = getattr(settings, 'ADDTHIS_DATA_TRACK_CLICKBACK', True)

    return {
        'data_ga_property': data_ga_property,
        'data_ga_social': data_ga_social,
        'data_track_addressbar': data_track_addressbar,
        'data_track_clickback': data_track_clickback,
        'twitter_bitly': twitter_bitly,
        'twitter_via': twitter_via,
    }
