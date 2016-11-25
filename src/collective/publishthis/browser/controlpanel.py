# -*- coding: utf-8 -*-
from collective.publishthis import _
from collective.publishthis.interfaces import IPublishThisSettings
from plone.app.registry.browser import controlpanel


class PackageSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPublishThisSettings
    label = _(u'Publish This')
    description = _(u'Here you can modify the settings for collective.publishthis.')


class PackageSettingsControlPanel(controlpanel.ControlPanelFormWrapper):

    form = PackageSettingsEditForm
