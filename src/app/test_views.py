# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render 
#from django.shortcuts import render_to_response
from django.http import HttpResponse
#from app.forms import MyForm
#from app.forms import PersonForm
#from app.forms import SampleForm
#from app.forms import ContactForm
from app.models import ContactForm
from app.models import Contact
#from django.views.generic import CreateView, UpdateView
#from app.models import Person
from django.views.generic import FormView
from django.http import HttpResponseRedirect
#from .forms import NameForm
from datetime import datetime
from datetime import date


class TestRequest:
	_env = {}

	@classmethod
	def test_request(cls, request):
		query_dict = request.POST.copy()
		cls._env["query_dict"] = query_dict
		return render(request,"test_request.html",{"env":cls._env})

