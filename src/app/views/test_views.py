# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render 
from datetime import datetime
from datetime import date
import app.logs.app_logging as logging

logger = logging.get_logger(__name__)


class TestRequest:
	_env = {}

	@classmethod
	def test_request(cls, request):
		logger.debug("test_request called")
		query_dict = request.POST.copy()
		cls._env["query_dict"] = query_dict
		return render(request,"test_request.html",{"env":cls._env})

