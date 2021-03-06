# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models.contact_models import Contact


class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['id']}),
	(None, {'fields': ['name']}),
	(None, {'fields': ['email']}),
	(None, {'fields': ['message']}),
	(None, {'fields': ['datetime']}),
	]
	list_display = ('id', 'name', 'email','message','datetime')

admin.site.register(Contact,ContactAdmin)

