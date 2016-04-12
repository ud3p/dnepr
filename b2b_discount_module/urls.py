from django.conf.urls import patterns, include, url
from django.contrib import admin
from b2b_discount_module import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
