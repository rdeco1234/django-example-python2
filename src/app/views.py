# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render 
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app.forms import MyForm
from app.forms import PersonForm
from app.forms import SampleForm
from django.views.generic import CreateView, UpdateView
from app.models import Person

def contact(request):
	if request.method == 'POST':
		form = MyForm(request.POST)

		if form.is_valid():
			message = 'OK'
		else:
			message = 'NG'
		d = {
			'form' : form,
			'message' : message,
		}
		return render(request,"response.html",d) 
		#return render(request,"test.html")
 
	else:
		form = MyForm({'name':'Keisuke', 'email':'dadosan@keicode.com', 'message': 'Hello, Django Form!'})

		return render(request,"contact.html",{'form1': form}) 
		#return HttpResponse(form.as_table())

def hello_template(request):
	#return render(request, 'index.html')
	return render(request, 'test.html')

class PersonCreateView(CreateView):
	model = Person
	form_class = PersonForm
	template_name = 'form.html'

def hello_forms2(request):
    d = {
        'form': forms.SampleForm(),
    }
    return render(request, 'form_samples.html', d)
