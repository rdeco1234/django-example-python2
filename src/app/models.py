# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Contact(models.Model):
    con = (
        (u"1",u"test1"),
        (u"2",u"test2"),
        (u"3",u"test3"),
        )
    name = models.CharField(u"name",max_length=50)
    old = models.PositiveIntegerField(u"name")
    content = models.CharField(u"contents",max_length=2, choices=con, default=None)

    def __unicode__(self):
        return self.name
