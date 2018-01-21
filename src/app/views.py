from __future__ import unicode_literals

from django.shortcuts import render 
from django.http import HttpResponse
from app.forms import MyForm

def contact(request):
	form = MyForm()
	return HttpResponse(form.as_table())
