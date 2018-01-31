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

#def contact(request):
	#name = request.POST['name']
#	if request.method == 'POST':
#		form = MyForm(request.POST)
#		text = 'tetete'
#
#		if form.is_valid():
#			message = 'OK'
#		else:
#			message = 'NG'

#	name = request.POST.get('name')
#	message = request.POST.get('message')
#	email = request.POST.get('email')

	#form = MyForm(request.POST)
#		form = MyForm(request.POST)
#		if form.is_valid():
#			name = form.cleaned_data['name']
#			form.vote()
#	else:
#		if 'name' in request.GET:
#			name = request.GET['name']
#		else:
#			name = 'jjj'

#	dict = {
#		'name':name,
#		'email':email,
#		'message':massage,
#	}

#	return render(request,"response.html",{'form':request.POST.get('name','ccc'),'name':name}) 
#	return render(request,"response.html",{'form':request.POST.get('name','ccc'),'name':name}) 

#		#return render(request,"test.html")
# 
#	else:
#		form = MyForm({'name':'Keisuke', 'email':'dadosan@keicode.com', 'text': 'Hello, Django Form!'})
#
#		return render(request,"contact.html",{'form1': form}) 
		#return HttpResponse(form.as_table())

#def hello_template(request):
#	#return render(request, 'index.html')
#	return render(request, 'test.html')

#class PersonCreateView(CreateView):
#	model = Person
#	form_class = PersonForm
#	template_name = 'form.html'
#	success_url = "/"

#def hello_forms2(request):
#    d = {
#        'form': forms.SampleForm(),
#    }
#    return render(request, 'form_samples.html', d)

#class ContactView(FormView):
#	template_name = 'contact_form.html'
#	form_class = ContactForm
#	success_url = '/app/thanks/'
#
#	def form_valid(self, form_class):
#		pass
#		form_class.send_mail()
#		return super(ContactView, self).form_valid(form_class)

class ContactView:

	@classmethod
	def get_name(cls, request):

		if request.method == 'POST':
			columns_dict = request.POST.copy()

			# check contact count
			email = columns_dict.__getitem__('email')
			ret = cls._check_count_per_day(email)
			if not ret["status"]:
				err_message = ret["message"]
				return render(request, 'error.html',{'message':err_message})

			# id and datetime setting
			if not columns_dict.__contains__('id'):
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
				return render(request, 'response.html')

			else:
				return render(request, 'error.html',{'debug':columns_dict})

		else:
			#if 'name' in request.GET:
			#	name = request.GET['name']
			#	return render(request, 'response.html')
			#else:
			form = ContactForm()
			return render(request, 'name.html', {'form': form})

		return render(request, 'error.html')


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
		

