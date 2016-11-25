**********************
collective.publishthis
**********************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

Publish This provides an easy way to grab text and images from any website and publish at your Plone site.

This package is heavly inspired on Wordpress plugin `Press This`_.

Mostly Harmless
===============

.. image:: http://img.shields.io/pypi/v/collective.publishthis.svg
   :target: https://pypi.python.org/pypi/collective.publishthis

.. image:: https://img.shields.io/travis/simplesconsultoria/collective.publishthis/master.svg
    :target: http://travis-ci.org/simplesconsultoria/collective.publishthis

.. image:: https://img.shields.io/coveralls/simplesconsultoria/collective.publishthis/master.svg
    :target: https://coveralls.io/github/simplesconsultoria/collective.publishthis

These are some sites using ``collective.publishthis``:

* `CartaCapital <http://www.cartacapital.com.br/>`_ (BR)

Got an idea? Found a bug? Let us know by `opening a support ticket <https://github.com/simplesconsultoria/collective.publishthis/issues>`_.

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.publishthis

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.publishthis`` and click the 'Activate' button.

.. Note::
    You may have to empty your browser cache and save your resource registries in order to see the effects of the product installation.

Usage
-----

At the control panel, select the content type to use and create the bookmarklet dragging the link into the bookmarks toolbar of your browser.

.. figure:: https://raw.github.com/collective/collective.publishthis/master/docs/controlpanel.png
    :align: center
    :height: 640px
    :width: 768px

    Publish This Control Panel.

After bookmark creation, visit your favorite news site, and find a nice article to copy, select the text of the page, and click on the bookmarklet.

.. figure:: https://raw.github.com/collective/collective.publishthis/master/docs/article.png
    :align: center
    :height: 640px
    :width: 768px

    Article to copy.

It will open a new window to review the grabbed content and create the new item in your Plone site.

.. figure:: https://raw.github.com/collective/collective.publishthis/master/docs/content_creation.png
    :align: center
    :height: 640px
    :width: 768px

    Create new content.

How does it work
----------------

When you grab your bookmarklet, the address of your site is attached into the javascript code of the bookmarklet, what makes possible to have more than one bookmarklet to publish in more than one Plone site.

At the usage time, the bookmarklet sends to your Plone site the selected text, title and URL of the page.  We pass these information into the default Plone creation item factory to create the new item in your Plone site.

Todo
----

* Create bookmarklet link at controlpanel.
* Create view to handle the new window and redirect into the content type factory.
* Add a step to select in what folder the content should be created.
* Add a step to select image to extract.
* Create an adapter for collective.nitf to extract more than one image.

.. _`Press This`: https://en.support.wordpress.com/press-this/
