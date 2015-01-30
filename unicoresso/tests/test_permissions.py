from django.test import TestCase
from sso import permissions
from django.contrib.auth.models import User
from unicoresso.models import AuthorizedSite


class customAttributesTest(TestCase):

    def test_group_access(self):
        user = User.objects.create(first_name='foo')
        site = AuthorizedSite.objects.create(site='foobar.com')
        self.assertEqual(
            permissions.custom_attributes(user, site)['has_perm'], False)

    def test_correct_user(self):
        user = User.objects.create(first_name='foo')
        site = AuthorizedSite.objects.create(site='foobar.com')
        self.assertEqual(
            permissions.custom_attributes(user, site)['givenName'], 'foo')

    def test_correct_group(self):
        user = User.objects.create(first_name=' ')
        site = AuthorizedSite.objects.create(site='foobar.com')
        self.assertEqual(
            permissions.custom_attributes(user, site)['group'].count(), 0)
