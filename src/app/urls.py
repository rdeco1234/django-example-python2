# -*- coding:utf-8 -*-

from django.conf.urls import include, url
from app.views import contact
from app.views.NameView import get_name
#from app.views import PersonCreateView
#from app.views import hello_template
#from app.views import hello_forms2
from app.views import ContactView 
from django.contrib import admin

urlpatterns = [
#    url(r'^mail/', contact),
#	url(r'create/$', PersonCreateView.as_view()),
#	url(r'template$', hello_template, name='hello_template'),
#    url(r'^form_samples/$', hello_forms2, name='hello_forms2'),
	url(r'^contact/$', ContactView.as_view(), name='ContactView'),
	url(r'^contact2/$', ContactView.as_view(), name='ContactView'),
	url(r'^thanks/$', get_name),
	url(r'^your-name/$', get_name),
]
