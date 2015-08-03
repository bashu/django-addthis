==============
django-addthis
==============

A simple integration of the `AddThis <http://www.addthis.com>`_ social sharing widget for Django projects.

Requirements
============

- Python 2.5+
- Django 1.4+

Installation
============

#.  Install the latest stable version using ``pip``:

    .. code:: shell

        pip install django-addthis

#.  Add ``addthis`` to your ``INSTALLED_APPS`` setting:

    .. code:: python

        INSTALLED_APPS = (
            ...
            'addthis',
        )

Configuration
=============

#.  The ``addthis_widget`` template tag requires a site *profile id*. ``pub_id``. Either pass it as ``pub_id``, or set ``PUB_ID`` in your ``ADDTHIS_SETTINGS`` settings dictionary:

    .. code:: python

        ADDTHIS_SETTINGS = {
            'PUB_ID': 'xx-xxxxxxxxxxxxxxxx',
            ...
        }

    The site *profile id* can be found by visiting its Profile Options page on `AddThis <http://www.addthis.com>`_ (**ID:**).

#.  There are a few `configuration options <http://support.addthis.com/customer/portal/articles/1337994-the-addthis_config-variable>`_ for django-addthis that can be placed in your ``ADDTHIS_SETTINGS`` settings dictionary:

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

Basic Usage
===========

#.  Load the tag library:

    .. code:: html

        {% load addthis %}

    You can pass these options as arguments:

    ========================= ========================= =========================
    Option                    Default                   Description
    ========================= ========================= =========================
    pub_id                                              Site *profile id* (see configuration above).
    ========================= ========================= =========================

#.  Load the widget:

    .. code:: html

        {% addthis_widget %}

#.  Visit the AddThis `Get the Code <http://www.addthis.com/get>`_ page and create/generate your social sharing code, e.g:

    .. code:: html

        <!-- Go to www.addthis.com/dashboard to customize your tools -->
        <div class="addthis_sharing_toolbox"></div>

    Be sure to omit the:

    .. code:: html

        <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=xx-xxxxxxxxxxxxxxxx"></script>

    part of the (generated) code as the ``addthis_widget`` template tag takes care of this.

Example
=======

.. code:: html

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

    </html>
