# encoding=utf-8

from django.db import models

class Todo(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = u"ToDo"
        ordering = ("id", )

    name = models.CharField(u"タイトル",max_length=100)
    description = models.TextField(u"詳細", blank=True)
    created_at = models.DateTimeField(u"登録日", auto_now_add=True)
    finished_at = models.DateTimeField(u"完了日", blank=True, null=True)
