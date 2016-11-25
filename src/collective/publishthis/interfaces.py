# -*- coding: utf-8 -*-
from collective.publishthis import _
from zope import schema
from zope.interface import Interface


class IPublishThisLayer(Interface):

    """A layer specific for this add-on product."""


class IPublishThisSettings(Interface):

    """Schema for the control panel form."""

    content_type = schema.Choice(
        title=_(u'Content Type'),
        description=_(u'Content type to be created using Publish This.'),
        required=True,
        vocabulary=u'plone.app.vocabularies.UserFriendlyTypes',
        default=u'News Item'
    )
