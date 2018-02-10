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


class ContactView:
	_env = {}

	@classmethod
	def get_name(cls, request):

		if request.method == 'POST':
			columns_dict = request.POST.copy()

			email = columns_dict.__getitem__('email')
			name = columns_dict.__getitem__('name')
			# check contact count
			ret = cls._check_count_per_day(email)
			if not ret["status"]:
				err_message = ret["message"]
				return render(request, 'error.html',{'message':err_message})

			# id and datetime setting
			if not columns_dict.__getitem__('id'):
				# random TODO
				import random
				num = random.randrange(10**3,10**4)
				columns_dict.__setitem__('id', str(num))
				# datetime
				now = datetime.now()
				columns_dict.__setitem__('datetime', now)

			# create form
			form = ContactForm(columns_dict)
#			for 'id' in form.fields:
#				form.fields['id'].widget = forms.HiddenInput()
			if form.is_valid():
				form.send_mail()
				form.save()
				return render(request, 'response.html',{"env":cls._env})

			else:
				return render(request, 'error.html',{'debug':columns_dict,'message':"invalid_form"})

		else:
			#if 'name' in request.GET:
			#	name = request.GET['name']
			#	return render(request, 'response.html')
			#else:
			form = ContactForm()
			return render(request, 'name.html', {'form': form})

		return render(request, 'error.html',{'message':"internal error"})


	@classmethod
	def _check_count_per_day(cls, email):
		ret = {"status":True, "message":""}

		today = date.today()

		year = today.year
		month = today.month
		day = today.day

		query = Contact.objects.filter(email__exact=email)
		query = query.filter(datetime__year=year)
		query = query.filter(datetime__month=month)
		query = query.filter(datetime__day=day)

		if len(query) > 10:
			#TODO error process
			ret["status"] = False
			ret["message"] = "over 10 contact"
			return ret

		return ret
		

