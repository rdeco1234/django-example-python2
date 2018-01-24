# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render 
from django.shortcuts import render_to_response
from django.http import HttpResponse
#from app.forms import MyForm
#from app.forms import PersonForm
#from app.forms import SampleForm
from app.forms import ContactForm
#from django.views.generic import CreateView, UpdateView
#from app.models import Person
from django.views.generic import FormView

def contact(request):
#	if request.method == 'POST':
#		form = MyForm(request.POST)
#		text = 'tetete'
#
#		if form.is_valid():
#			message = 'OK'
#		else:
#			message = 'NG'
#	d = {
#		'message' : message,
#		'email' : email,
#	}
	return render(request,"response.html") 
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

class ContactView(FormView):
	template_name = 'contact_form.html'
	form_class = ContactForm
	success_url = '/app/thanks/'

	def form_valid(self, form_class):
		form_class.send_mail()
		return super(ContactView, self).form_valid(form_class)


