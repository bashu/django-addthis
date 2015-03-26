==============
django-addthis
==============

A simple integration of the `AddThis <http://www.addthis.com>`_ social sharing
widget for Django projects.

Requirements
============

- Python 2.5+
- Django 1.4+

Installation
============

#.  Install the latest stable version using ``pip``

    .. code:: shell

        pip install django-addthis

    Alternatively, if you want to install the sources directly off the repository

    .. code:: shell

        pip install git+https://github.com/raymondwanyoike/django-addthis.git#egg=django-addthis

#.  Add ``addthis`` to your ``INSTALLED_APPS`` setting

    .. code:: python

        INSTALLED_APPS = (
            ...
            'addthis',
        )

Configuration
=============

#.  The ``addthis_widget`` template tag requires a ``pub_id``. You must either
    pass it as an argument or set ``PUB_ID`` in your ``ADDTHIS_SETTINGS``
    settings dictionary. Setting this value means that you can omit the ``pub_id``
    argument when invoking the template tag

    .. code:: python

        ADDTHIS_SETTINGS = {
            'PUB_ID': 'xx-xxxxxxxxxxxxxxxx',
            ...
        }

#.  There are a few `other configuration options <http://support.addthis.com/customer/portal/articles/1337994-the-addthis_config-variable/>`_
    for django-addthis that can be placed in your ``ADDTHIS_SETTINGS`` settings
    dictionary:

    ============================ ============================
    Django Setting               Default
    ============================ ============================
    USERNAME                     N/A
    SERVICES_EXCLUDE             N/A
    SERVICES_COMPACT             N/A
    SERVICES_EXPANDED            N/A
    SERVICES_CUSTOM              N/A
    UI_CLICK                     False
    UI_DELAY                     0
    UI_HOVER_DIRECTION           0
    UI_LANGUAGE                  N/A
    UI_OFFSET_TOP                0
    UI_OFFSET_LEFT               0
    UI_HEADER_COLOR              N/A
    UI_HEADER_BACKGROUND         N/A
    UI_COBRAND                   N/A
    UI_USE_CSS                   True
    UI_USE_ADDRESSBOOK           False
    UI_508_COMPLIANT             False
    DATA_TRACK_CLICKBACK         True
    DATA_GA_TRACKER              N/A
    ============================ ============================


Basic Usage
===========

#.  Load the tag library

    .. code:: html

        {% load addthis %}

#.  Set the js config (API)

    .. code:: html

        {% addthis_config %}

#.  Load the js widget

    .. code:: html

        {% addthis_widget pub_id='xx-xxxxxxxxxxxxxxxx' %}

    or with ``PUB_ID`` defined in your ``ADDTHIS_SETTINGS`` settings
    dictionary

    .. code:: html

        {% addthis_widget %}

#.  Visit the AddThis `Get the Code <http://www.addthis.com/get>`_ page and
    create/generate/get your social sharing code, e.g

    .. code:: html

        <!-- Go to www.addthis.com/dashboard to customize your tools -->
        <div class="addthis_sharing_toolbox"></div>

    Be sure to omit the

    .. code:: html

        <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=xx-xxxxxxxxxxxxxxxx"></script>

    part of the (generated) code as the ``addthis_widget`` template tag takes
    care of this.

Example
=======

.. code:: html

    {% load addthis %}<!DOCTYPE html>

    <html>

    <head>
      <meta charset="utf-8">
      <title>django-addthis Example</title>

      {% addthis_config %}
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

    </html>
