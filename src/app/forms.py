# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.conf import settings
#from app.models import Person

#class MyForm(forms.Form):
#	name = forms.CharField()
#	email = forms.EmailField()
#	text = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)

	def send_mail(self):
		pass
#		subject = self.cleaned_data['name']
#		message = self.cleaned_data['message']
#		from_email = settings.EMAIL_HOST_USER
#		to = [settings.EMAIL_HOST_USER]
#
#		send_mail(subject, message, from_email, to)


#class PersonForm(forms.Form):
#    class Meta:
#        model = Person
#        fields = ("name", "age")


#class SampleForm(forms.Form):
#    class Meta:
#        model = Person
#        fields = ("name", "age")