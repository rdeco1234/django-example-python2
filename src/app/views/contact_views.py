# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render 
from django.http import HttpResponse
from app.forms.contact_forms import ContactForm
from app.models.contact_models import Contact
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from datetime import datetime
from datetime import date


class ContactView:

	def __init__(self):
		# Response information
		self._env = {}
		# DB instanse
		self._contact_models = Contact()

	def get_name(self, request):

		if request.method == 'POST':
			columns_dict = request.POST.copy()

			#POST information
			email = columns_dict.__getitem__('email')
			name = columns_dict.__getitem__('name')

			# check contact count
			ret = self._check_count_per_day(email)
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
			if form.is_valid():
				form.send_mail()
				# DB save
				form.save()
				self._env["name"] =  name
				return render(request, 'response.html',{"env":self._env})

			else:
				return render(request, 'error.html',{'debug':columns_dict,'message':"invalid_form"})

		else:
			form = ContactForm()
			return render(request, 'contact.html', {'form': form})

		return render(request, 'error.html',{'message':"internal error"})


	#@classmethod
	def _check_count_per_day(self, email):

		ret = {"status":True, "message":""}

		today = date.today()
		records = self._contact_models.get_email_filtered_by_day(email, today)

		if len(records) > 10:
			#TODO error process
			ret["status"] = False
			ret["message"] = "over 10 contact"
			return ret

		return ret
		

