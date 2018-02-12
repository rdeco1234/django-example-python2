# coding : urf-8

import logging.config
import app.configs.logging_config as log_conf


def get_logger(*args):

	# settings
	#logging.config.fileConfig(log_conf.LOG_FILE_PATH + log_conf.LOG_FILE_NAME)
	logging.config.fileConfig('/home/rdeco/www/rdeco.sakura.ne.jp/django-example-python2-dev/src/app/configs/conf/logging.conf')
	logger = logging.getLogger(*args)

	return logger

