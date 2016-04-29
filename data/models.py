from __future__ import unicode_literals

from django.db import models

# Create your models here.

class notify(models.Model):
	string1 = models.CharField(max_length=100, null=True)
	string2 = models.CharField(max_length=100, null=True)
	string3 = models.CharField(max_length=100, null=True)
	string4 = models.CharField(max_length=100, null=True)