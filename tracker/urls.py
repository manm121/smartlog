from django.contrib import admin
from django.urls import include, path
from tracker import views

urlpatterns = [
    path('', views.index, name="index"),
    path('master', views.master, name="master"),
    path('newissue', views.newissue, name="newissue"),
    path('process_request', views.process_request, name="process_request"),
]