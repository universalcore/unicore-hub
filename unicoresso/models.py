from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

	def __str__(self):
		return self.username

class Repo(models.Model):
	url = models.CharField(max_length=30)
	users = models.ManyToManyField(User)

	def __str__(self):
		return self.url