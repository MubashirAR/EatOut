from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my-profile/$', views.profile),
    url(r'^edit/$', views.edit),
    url(r'^ratings/$', views.ratings),    
]