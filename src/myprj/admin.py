# encoding=utf-8

from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "finished_at")

admin.site.register(Todo, TodoAdmin)
