# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Restaurant

# Create your views here.

def profile(request):
	restaurant = Restaurant.objects.get(name='Nice Resto')
	return render(request, 'users/profile.html')

def edit(request):
	return render(request, 'users/edit.html')

def ratings(request):
	return render(request, 'users/ratings.html')

def rate(request):
	return render(request, 'users/ratings.html')