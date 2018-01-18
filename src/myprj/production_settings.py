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

STATIC_URL = '/static/'
STATIC_ROOT = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs/static'
