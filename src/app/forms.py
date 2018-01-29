# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.conf import settings
#from app.models import Person

class MyForm(forms.Form):

	def vote(self):
		assert(self.is_valid())
		#name = self.cleaned_data['name']
		#name.save()

#class ContactForm(forms.Form):
#	name = forms.CharField()
#	email = forms.EmailField()
#	message = forms.CharField(widget=forms.Textarea)
#
#	def send_mail(self):
#		pass
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

class ContactForm(forms.Form):
	name = forms.CharField(label='name', max_length=30)
	email = forms.EmailField()
	subject = forms.CharField(label='subject', max_length=100)
	message = forms.CharField(
					label='message',
					widget=forms.Textarea,
					max_length=400
				)

	def send_mail(self, data):
		subject = data['subject']
		name = data['name']
		message = data['message']
		send_message = "name : "+ name + "\n"
		send_message += "message : "+ message + "\n"
		from_email = settings.EMAIL_HOST_USER
		to = [settings.EMAIL_HOST_USER]

		send_mail(subject, send_message, from_email, to)
