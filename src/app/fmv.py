# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.conf import settings

class MyCreateView(CreateView):
	model = MyModel

	def form_valid(self, form):
		messages.success(self.request, "saved!")
		return super().form_valid(form)

	def form_invalid(self. form):
		message.warning(self, request, "couldn't saved")
		return super().form_invalid(form)

