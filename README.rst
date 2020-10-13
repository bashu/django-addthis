django-addthis
==============

A simple integration of the `AddThis <http://www.addthis.com>`_ social sharing widget for Django_ projects.

Authored by `Raymond Wanyoike <https://github.com/rwanyoike>`_, and some great
`contributors <https://github.com/bashu/django-addthis/contributors>`_.

.. image:: https://img.shields.io/pypi/v/django-addthis.svg
    :target: https://pypi.python.org/pypi/django-addthis/

.. image:: https://img.shields.io/pypi/dm/django-addthis.svg
    :target: https://pypi.python.org/pypi/django-addthis/

.. image:: https://img.shields.io/github/license/bashu/django-addthis.svg
    :target: https://pypi.python.org/pypi/django-addthis/

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code:: shell

    pip install django-addthis

Setup
=====

You'll need to add ``addthis`` to ``INSTALLED_APPS`` in your project's ``settings.py`` file:

.. code:: python

    INSTALLED_APPS += [
        'addthis',
    ]

Configuration
=============

The ``addthis_widget`` template tag requires a site *profile id*: ``pub_id``. Either pass it as ``pub_id``, or set ``PUB_ID`` in your ``ADDTHIS_SETTINGS`` settings dictionary:

.. code:: python

    ADDTHIS_SETTINGS = {
        'PUB_ID': 'xx-xxxxxxxxxxxxxxxx',
        ...
    }

The site *profile id* can be found by visiting its Profile Options page on `AddThis <http://www.addthis.com>`_ (**ID:**).

There are a few `configuration options <http://support.addthis.com/customer/portal/articles/1337994-the-addthis_config-variable>`_ for ``addthis`` that can be placed in your ``ADDTHIS_SETTINGS`` settings dictionary:

============================ ============================
Option                       Default
============================ ============================
USERNAME
SERVICES_EXCLUDE
SERVICES_COMPACT
SERVICES_EXPANDED
SERVICES_CUSTOM
UI_CLICK                     False
UI_DELAY                     0
UI_HOVER_DIRECTION           0
UI_LANGUAGE
UI_OFFSET_TOP                0
UI_OFFSET_LEFT               0
UI_HEADER_COLOR
UI_HEADER_BACKGROUND
UI_COBRAND
UI_USE_CSS                   True
UI_USE_ADDRESSBOOK           False
UI_508_COMPLIANT             False
DATA_TRACK_CLICKBACK         True
DATA_GA_TRACKER
============================ ============================

Please see the ``example`` application. This application is used to
manually test the functionalities of this package. This also serves as
a good example.

You need Django 1.8 or above to run that. It might run on older versions but that is not tested.

Usage
=====

#.  First of all, load the ``addthis`` in every template where you want to use it:

    .. code:: html+django

        {% load addthis %}

    You can pass these options as arguments:

    ========================= ========================= =========================
    Option                    Default                   Description
    ========================= ========================= =========================
    pub_id                                              Site *profile id* (see configuration above).
    ========================= ========================= =========================

    then load the widget:

    .. code:: html+django

        {% addthis_widget %}

#.  Visit the AddThis `Get the Code <http://www.addthis.com/get>`_ page and create/generate your social sharing code, e.g:

    .. code:: html+django

        <!-- Go to www.addthis.com/dashboard to customize your tools -->
        <div class="addthis_sharing_toolbox"></div>

    Be sure to omit the:

    .. code:: html+django

        <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=xx-xxxxxxxxxxxxxxxx"></script>

    part of the (generated) code as the ``addthis_widget`` template tag takes care of this.

Example
-------

.. code:: html+django

    {% load addthis %}

    <!DOCTYPE html>

    <html>
    <head>
      <meta charset="utf-8">
      <title>django-addthis Example</title>
    </head>

    <body>
      <!-- Go to www.addthis.com/dashboard to customize your tools -->
      <div class="addthis_sharing_toolbox"></div>

      <p>Well, the way they make shows is, they make one show. That show's
      called a pilot. Then they show that show to the people who make shows,
      and on the strength of that one show they decide if they're going to
      make more shows. Some pilots get picked and become television programs.
      Some don't, become nothing. She starred in one of the ones that became
      nothing.</p>

      <!-- Placed at the end of the document so the page load faster -->
      {% addthis_widget %}
    </body>
    </html

Contributing
------------

If you've found a bug, implemented a feature or customized the template and
think it is useful then please consider contributing. Patches, pull requests or
just suggestions are welcome!

License
-------

``django-addthis`` is released under the GNU GPL v3 license.

.. _django: https://www.djangoproject.com
