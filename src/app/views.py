# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render 
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app.forms import MyForm
from app.forms import NameForm
#from app.forms import PersonForm
#from app.forms import SampleForm
from app.forms import ContactForm
#from django.views.generic import CreateView, UpdateView
#from app.models import Person
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from .forms import NameForm


def contact(request):
	#name = request.POST['name']
	if request.method == 'POST':
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
		form = MyForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			form.vote()
	else:
		if 'name' in request.GET:
			name = request.GET['name']
		else:
			name = 'jjj'

#	dict = {
#		'name':name,
#		'email':email,
#		'message':massage,
#	}

	return render(request,"response.html",{'form':request.POST.get('name','ccc'),'name':name}) 
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

class ContactView(FormView):
#	template_name = 'contact_form.html'
#	form_class = ContactForm
#	success_url = '/app/thanks/'

	def form_valid(self, form_class):
#		form_class.send_mail()
#		return super(ContactView, self).form_valid(form_class)

#class NameView(FormView):
def get_name(request):
	name = 'init'
    # if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			#return HttpResponseRedirect('/app/thanks?name=ccc')

			if 'your_name' in request.POST:
				postName = request.POST['your_name']
			else:
				postName = 'post_init'

			return HttpResponseRedirect('/app/thanks?name=' + postName)
    # if a GET (or any other method) we'll create a blank form
	else:
		if 'name' in request.GET:
			name = request.GET['name']
		else:
			name = 'get_init'

	 	form = NameForm()

	return render(request, 'name.html', {'form': form,'name':name})
