# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class Contact(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	subject = models.CharField(max_length=100)
	message = models.TextField()
	datetime = models.DateTimeField()


	def get_email_filtered_by_day(self, email, date_):
		year = date_.year
		month = date_.month
		day = date_.day

		_q = Contact.objects.filter(email__exact=email)
		_q = _q.filter(datetime__year=year)
		_q = _q.filter(datetime__month=month)
		query = _q.filter(datetime__day=day)

		return query

