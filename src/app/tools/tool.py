# coding : utf-8

import sys
import app.logs.app_logging as logging

logger = logging.get_logger(__name__)

def get_method_name():
	'''
	@param
	@return string method_name
	'''

	method_name = sys._getframe().f_code.co_name
	message = method_name
	logger.debug(message, module_=__name__)

	return method_name

