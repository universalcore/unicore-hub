from django.db import models
from django.contrib.auth.models import Group, User

class authorizedSite(models.Model):
	site = models.CharField(max_length=200)
	group = models.ManyToManyField(Group)

	def __str__(self):
		return self.site
