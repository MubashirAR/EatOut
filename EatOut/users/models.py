# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=12)
	DOB = models.DateField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	slug = models.SlugField()
	bio = models.TextField()
	profile_image = models.URLField()

# def __str__(self):
# 	return f'{self.first_name} {self.last_name}'

