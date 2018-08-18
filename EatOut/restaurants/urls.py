from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile),
    url(r'^edit/$', views.edit),
    url(r'^ratings/$', views.ratings),
    url(r'^rate/$', views.rate),  
]