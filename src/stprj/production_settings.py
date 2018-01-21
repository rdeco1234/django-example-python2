# encoding=utf-8

from .settings import *

DEBUG = False
ALLOWED_HOSTS = ["rdeco.sakura.ne.jp"]

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rdeco_db',
        'USER': 'rdeco',
        'PASSWORD': 'abcd-1234',
        'HOST': 'mysql303.db.sakura.ne.jp',
        'OPTIONS': {
               "init_command": "SET storage_engine=InnoDB",
        }
    }
}

INSTALLED_APPS = (
#	'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

STATIC_URL = '/static/'
STATIC_ROOT = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs/static'

#TEMPLAETE_DIR = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs/rdeco_hp'
TEMPLAETE_DIR = '/home/rdeco/www/rdeco.sakura.ne.jp/django-example-python2/src/app/template'
