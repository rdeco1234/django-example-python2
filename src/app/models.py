# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from django.core.mail import send_mail
from django.conf import settings

class Contact(models.Model):
#	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
#	email = models.EmailField(max_length=50)
	subject = models.CharField(max_length=100)
#	message = models.TextField()
#	datetime = models.DateTimeField()

	def __init__(self, data=[]):
		self.data = []
		if data:
			self.data = data


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
#			'id',
			'name',
#			'email',
			'subject',
#			'message',
#			'datetime',
		]

	def send_mail(self):
		if not self.data:
			return

		name = self.data['name']
		subject = self.data['subject']
#		subject = data['subject']
#		name = data['name']
#		message = data['message']
		send_message = "name : "+ name + "\n"
#		send_message += "email : "+ email + "\n"
#		send_message += "message : "+ message + "\n"
		from_email = settings.EMAIL_HOST_USER
		to = [settings.EMAIL_HOST_USER]

		send_mail(subject, send_message, from_email, to)

