# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#class Contact(models.Model):
#    con = (
#        (u"1",u"test1"),
#        (u"2",u"test2"),
#        (u"3",u"test3"),
#        )
#    name = models.CharField(u"name",max_length=50)
#    old = models.PositiveIntegerField(u"name")
#    content = models.CharField(u"contents",max_length=2, choices=con, default=None)

 #   def __unicode__(self):
 #       return self.name

#class Person(models.Model):
#	name = models.CharField(max_length=255)
#	age = models.IntegerField(default=25)
#
#class MyModel(models.Model):
#	name = models.CharField(max_length=255)
#	age = models.IntegerField(default=25)

class Author(models.Model):
	name = models.CharField(max_length=200)

	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'pk':self.pk})
