# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
	name = forms.CharField(label='name', max_length=30)
	email = forms.EmailField()
	subject = forms.CharField(label='subject', max_length=100)
	message = forms.CharField(
					label='message',
					widget=forms.Textarea,
					max_length=400
				)

	def send_mail(self):
		send_message = "name : "+ self.name + "\n"
		send_message += "email : "+ self.email + "\n"
		send_message += "message : "+ self.message + "\n"
		send_message += "datetime : "+ self.datetime + "\n"
		from_email = settings.EMAIL_HOST_USER
		to = [settings.EMAIL_HOST_USER]

		send_mail(subject, send_message, from_email, to)
