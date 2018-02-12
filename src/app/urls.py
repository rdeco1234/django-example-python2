# -*- coding:utf-8 -*-

from django.conf.urls import include, url
from app.views.contact_views import ContactView
from app.views.test_views import TestRequest
from django.contrib import admin

urlpatterns = [
	url(r'^thanks/$', ContactView.get_name),
	url(r'^contact/$', ContactView.get_name),
	url(r'^test/$', TestRequest.test_request),
]
