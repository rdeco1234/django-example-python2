# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from django.core.mail import send_mail
from django.conf import settings


class Contact(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	subject = models.CharField(max_length=100)
	message = models.TextField()
	datetime = models.DateTimeField()


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			'id',
			'name',
			'email',
			'subject',
			'message',
			'datetime',
		]
		widgets = {
			'id' : forms.HiddenInput(),
			'datetime' : forms.HiddenInput()
		}

	def send_mail(self):
#		name = self.data['name']
#		subject = self.data['subject']
#		subject = data['subject']
#		name = data['name']
#		message = data['message']
		name = self.cleaned_data['name']
		subject = self.cleaned_data['subject']
		email = self.cleaned_data['email']
		message = self.cleaned_data['message']
		send_message = "name : "+ name + "\n"
		send_message += "email : "+ email + "\n"
		send_message += "message : "+ message + "\n"
		from_email = settings.EMAIL_HOST_USER
		to = [settings.EMAIL_HOST_USER]

		send_mail(subject, send_message, from_email, to)


