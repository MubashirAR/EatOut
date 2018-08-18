# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField()
	description = models.TextField()
	location = models.TextField()
	area = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)

def __str__(self):
	return self.name