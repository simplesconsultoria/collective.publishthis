# -*- coding: utf-8 -*-
from collective.publishthis import _
from collective.publishthis.interfaces import IPublishThisSettings
from plone import api
from plone.app.registry.browser import controlpanel
from plone.z3cform import layout
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PackageSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPublishThisSettings
    label = _(u'Publish This')
    description = _(u'Here you can modify the settings for collective.publishthis.')


class PackageSettingsControlPanel(layout.FormWrapper):

    form = PackageSettingsEditForm
    index = ViewPageTemplateFile('controlpanel_layout.pt')

    @property
    def control_panel_url(self):
        portal = api.portal.get()
        return u'{0}/@@overview-controlpanel'.format(portal.absolute_url())

    @property
    def bookmarklet(self):
        return (
            'javascript:(function(){{'
            'window.open(\'{0}?'
            'url=\'+location.href+\'&'
            'title=\'+document.title+\'&'
            'text=\'+window.getSelection(),'
            '\'_blank\','
            '\'location,resizable,scrollbars,'
            'width=\'+window.outerWidth+\','
            'height=\'+window.outerHeight);}})()'
        ).format(self.url)

    @property
    def url(self):
        portal = api.portal.get()
        return u'{0}/@@publish-this'.format(portal.absolute_url())

    @property
    def title(self):
        portal = api.portal.get()
        return portal.Title()
