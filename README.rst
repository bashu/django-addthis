==============
Django AddThis
==============

This project is a simple integration of the AddThis social sharing widget for
quick implementation in Django projects.

Requirements
============

- Python 2.5+
- Django 1.4+

Installation
============

#. Install the latest stable version using ``pip``::

       pip install django-addthis

   Alternatively, if you want to install the sources directly off the repository::

       pip install git+https://github.com/raymondwanyoike/django-addthis.git#egg=django-addthis

   You may have to add the ``addthis`` directory to your Python path in the latter case.

#. Add ``addthis`` to your ``INSTALLED_APPS`` setting::

       INSTALLED_APPS = (
           ...
           'addthis',
       )

Configuration
=============

#. The ``addthis_widget`` template tag requires a ``pub_id``. You must either
   pass it as an argument or set ``ADDTHIS_PUB_ID`` in your settings. Setting
   this value means that you can omit the `pub_id` argument when invoking the
   template tag.

#. There are a few other configuration options for Django AddThis that can be
   placed in your settings:

   - ``ADDTHIS_DATA_GA_PROPERTY`` (or ``GOOGLE_ANALYTICS_PROPERTY_ID``) (String)
   - ``ADDTHIS_DATA_GA_SOCIAL`` (Boolean)
   - ``ADDTHIS_DATA_TRACK_ADDRESSBAR`` (Boolean)
   - ``ADDTHIS_DATA_TRACK_CLICKBACK`` (Boolean)
   - ``ADDTHIS_GA_TRACKING_ENABLED`` (Boolean)
   - ``ADDTHIS_TWITTER_BITLY`` (Boolean)
   - ``ADDTHIS_TWITTER_VIA`` (String)

Basic Usage
===========

#. Load the tag library::

       {% load addthis %}

#. Set the js config (API)::

       {% addthis_config %}

#. Load the js widget::

       {% addthis_widget pub_id=XXXXXXXXX %}

   or with ``ADDTHIS_PUB_ID`` defined in settings.py::

      {% addthis_widget %}

#. Visit the AddThis `Get the Code <http://www.addthis.com/get>`_ page and
   create/generate/get your social sharing code::

       <!-- AddThis Button BEGIN -->
       <div class="addthis_toolbox addthis_default_style addthis_32x32_style">
         <a class="addthis_button_preferred_1"></a>
         <a class="addthis_button_preferred_2"></a>
         <a class="addthis_button_preferred_3"></a>
         <a class="addthis_button_preferred_4"></a>
         <a class="addthis_button_compact"></a>
         <a class="addthis_counter addthis_bubble_style"></a>
      </div>
      <!-- AddThis Button END -->

   Be sure to omit the::

       <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=XXXXXXXXX"></script>

   part of the (generated) code as the ``addthis_widget`` template tag takes
   care of this.

Example
=======

::

    {% load addthis %}

    <html>
      <head>
        <title>Full Example</title>
        {% addthis_config %}
        {% addthis_widget %}
      </head>
      <body>
        <!-- AddThis Share Buttons BEGIN -->
        <div class="addthis_toolbox addthis_default_style addthis_32x32_style">
          <a class="addthis_button_preferred_1"></a>
          <a class="addthis_button_preferred_2"></a>
        </div>
        <!-- AddThis Share Buttons END -->

        <!-- AddThis Follow Buttons BEGIN -->
        <div class="addthis_toolbox addthis_32x32_style addthis_default_style">
          <a class="addthis_button_facebook_follow" addthis:userid="YOUR-PROFILE"></a>
          <a class="addthis_button_twitter_follow" addthis:userid="YOUR-USERNAME"></a>
        </div>
        <!-- AddThis Follow Buttons END -->
      </body>
    </html>
