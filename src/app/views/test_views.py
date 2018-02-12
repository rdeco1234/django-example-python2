# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render 
from datetime import datetime
from datetime import date


class TestRequest:
	_env = {}

	@classmethod
	def test_request(cls, request):
		query_dict = request.POST.copy()
		#cls._env["query_dict"] = query_dict
		cls._env["query_dict"] = aaa
		return render(request,"test_request.html",{"env":cls._env})

