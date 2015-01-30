from django.test import TestCase
from sso import permissions
from django.contrib.auth.models import Group, User
from unicoresso.models import authorizedSite

class customAttributesTest(TestCase):
	def test_group_access(self):
		user = User.objects.create(username='foo')
		site = authorizedSite.objects.create(site='foobar.com')
		self.assertEqual(permissions.custom_attributes(user, site)['has_perm'], False)


	def test_correct_user(self):
		user = User.objects.create(username='foo')
		site = authorizedSite.objects.create(site='foobar.com')
		self.assertEqual(permissions.custom_attributes(user, site)['givenName'], 'foo')





