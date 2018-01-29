# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Contact(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	email = models.EmailField()
	message = models.TextField()
	datetime = models.DateTimeField()

