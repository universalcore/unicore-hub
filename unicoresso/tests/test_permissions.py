from django.test import TestCase
from sso import permissions
from django.contrib.auth.models import User, Group
from unicoresso.models import AuthorizedSite


class customAttributesTest(TestCase):

    def test_group_access(self):
        user = User.objects.create(first_name='foo')
        site = AuthorizedSite.objects.create(site='http://foobar.com')
        self.assertEqual(
            permissions.custom_attributes(user, site.site)['has_perm'], False)

    def test_correct_user(self):
        user = User.objects.create(first_name='foo')
        site = AuthorizedSite.objects.create(site='http://foobar.com')
        self.assertEqual(
            permissions.custom_attributes(user, site.site)['givenName'], 'foo')

    def test_correct_group(self):
        user = User.objects.create(first_name=' ')
        site = AuthorizedSite.objects.create(site='http://foobar.com')
        self.assertEqual(
            len(permissions.custom_attributes(user, site.site)['groups']), 0)

    def test_wildcard_url(self):
        user = User.objects.create(first_name='foo')
        group = Group.objects.create(name='Unicef')
        user.groups.add(group)
        user.save()

        site = AuthorizedSite.objects.create(
            site='*.fflangola.qa-hub.unicore.io')
        site.group.add(group)
        site.save()

        attr = permissions.custom_attributes(
            user, 'htto://cms.tz.fflangola.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], True)
        self.assertEqual(attr['groups'], ['Unicef'])

        attr = permissions.custom_attributes(
            user, 'htto://cms.za.fflangola.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], True)

        attr = permissions.custom_attributes(
            user, 'htto://cms.za.ffl.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], False)

        attr = permissions.custom_attributes(
            user, 'htto://cms.za.gem.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], False)
