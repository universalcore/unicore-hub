from django.test import TestCase
from sso import permissions
from django.contrib.auth.models import User, Group
from unicoresso.models import AuthorizedSite


class customAttributesTest(TestCase):

    def test_group_access(self):
        user = User.objects.create(first_name='foo')
        attr = permissions.custom_attributes(user, 'http://foobar.com/')
        self.assertEqual(attr['has_perm'], False)

    def test_correct_user(self):
        user = User.objects.create(first_name='foo')
        attr = permissions.custom_attributes(user, 'http://foobar.com/')
        self.assertEqual(attr['givenName'], 'foo')

    def test_correct_group(self):
        user = User.objects.create(first_name=' ')
        attr = permissions.custom_attributes(user, 'http://foobar.com/')
        self.assertEqual(len(attr['groups']), 0)

        group = Group.objects.create(name='The Foo')
        user.groups.add(group)
        user.save()
        site = AuthorizedSite.objects.create(site='http://foobar.com/*')
        site.group.add(group)
        site.save()

        attr = permissions.custom_attributes(user, 'http://foobar.com/')
        self.assertEqual(len(attr['groups']), 1)
        self.assertEqual(attr['groups'], ['The Foo'])

    def test_wildcard_url(self):
        user = User.objects.create(first_name='foo')
        group = Group.objects.create(name='Unicef')
        user.groups.add(group)
        user.save()

        site = AuthorizedSite.objects.create(
            site='http://*.fflangola.qa-hub.unicore.io/*')
        site.group.add(group)
        site.save()

        attr = permissions.custom_attributes(
            user, 'http://cms.tz.fflangola.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], True)
        self.assertEqual(attr['groups'], ['Unicef'])

        attr = permissions.custom_attributes(
            user, 'http://cms.za.fflangola.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], True)

        attr = permissions.custom_attributes(
            user, 'http://cms.za.ffl.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], False)

        attr = permissions.custom_attributes(
            user, 'http://cms.za.gem.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], False)

    def test_exact_match_site(self):
        user = User.objects.create(first_name='foo')
        group = Group.objects.create(name='MAMA')
        user.groups.add(group)
        user.save()

        site = AuthorizedSite.objects.create(
            site='http://cms.za.mama.qa-hub.unicore.io/*')
        site.group.add(group)
        site.save()

        attr = permissions.custom_attributes(
            user, 'http://cms.za.mama.qa-hub.unicore.io/login/')
        self.assertEqual(attr['has_perm'], True)
        self.assertEqual(attr['groups'], ['MAMA'])
