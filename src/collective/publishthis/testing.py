# -*- coding: utf-8 -*-
# FIXME: https://github.com/plone/plone.recipe.codeanalysis/issues/198  # noqa: T000
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting  # noqa: I001
from plone.app.testing import IntegrationTesting  # noqa: I001
from plone.app.testing import PLONE_FIXTURE  # noqa: I001
from plone.app.testing import PloneSandboxLayer  # noqa: I001
from plone.testing import z2


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.publishthis
        self.loadZCML(package=collective.publishthis)

    def setUpPloneSite(self, portal):
        self.applyProfile(
            portal, 'collective.publishthis:default')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name='collective.publishthis:Integration')

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name='collective.publishthis:Functional')

ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='collective.publishthis:Robot',
)
