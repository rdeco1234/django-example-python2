# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.conf import settings

class MyForm(forms.Form):
#	name = forms.CharField()
#	email = forms.EmailField()
#	message = forms.CharField(widget=forms.Textarea)
	your_name = forms.CharField(
	label='name',
	max_length=20,
	required=True,
	widget=forms.TextInput()
    )

	def send_email(self):
		subject = self.cleaned_data['name']
		message = self.cleaned_data['message']
		from_email = settings.EMAIL_HOST_USER
		to = [settings.EMAIL_HOST_USER]

		send_mail(subject, message, from_email, to)


class PersonForm(forms.Form):
	word = forms.CharField(max_length=250)


