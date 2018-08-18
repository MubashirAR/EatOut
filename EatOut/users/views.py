
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import User
# Create your views here.

def profile(request):
	return render(request, 'users/profile.html')

def edit(request):
	return render(request, 'users/edit.html')

def ratings(request):
	return render(request, 'users/ratings.html')