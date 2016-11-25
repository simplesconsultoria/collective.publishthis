# -*- coding: utf-8 -*-
from collective.publishthis.config import PROJECTNAME
from collective.publishthis.interfaces import IPublishThisLayer
from collective.publishthis.testing import INTEGRATION_TESTING
from plone import api
from plone.browserlayer.utils import registered_layers

import unittest


class InstallTestCase(unittest.TestCase):

    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = self.portal['portal_quickinstaller']
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer(self):
        self.assertIn(IPublishThisLayer, registered_layers())

    def test_setup_permission(self):
        permission = 'collective.publishthis: Setup'
        roles = self.portal.rolesOfPermission(permission)
        roles = [r['name'] for r in roles if r['selected']]
        expected = ['Manager', 'Site Administrator']
        self.assertListEqual(roles, expected)

    def test_version(self):
        profile = 'collective.publishthis:default'
        setup_tool = self.portal['portal_setup']
        self.assertEqual(
            setup_tool.getLastVersionForProfile(profile), (u'1',))


class UninstallTestCase(unittest.TestCase):

    """Ensure product is properly uninstalled."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer_removed(self):
        self.assertNotIn(IPublishThisLayer, registered_layers())
