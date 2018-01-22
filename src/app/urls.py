# -*- coding:utf-8 -*-

from django.conf.urls import include, url
from app.views import contact
from app.views import PersonCreateView
from app.views import hello_template
from django.contrib import admin

urlpatterns = [
    url(r'^mail/', contact),
	url(r'create/', PersonCreateView.as_view()),
	url(r'template$', hello_template, name='hello_template'),
]
