# encoding=utf-8

from .settings import *

DEBUG = True
TEMPLATE_DEBUG = True
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
	'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'bootstrap3'
)

STATIC_URL = '/static/'
STATIC_ROOT = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs/static'

#TEMPLATE_DIR = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs/rdeco_hp'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'template'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


LOGGING = {
    'version': 1,
    'formatters': {
        'all': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "asctime:%(asctime)s",
                "module:%(module)s",
                "message:%(message)s",
                "process:%(process)d",
                "thread:%(thread)d",
            ])
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
            'formatter': 'all',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler', 
            'formatter': 'all'
        },
    },
    'loggers': {
        'command': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    },
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
#EMAIL_HOST_USER = 'gragrapopbreaker@gmail.com'
#EMAIL_HOST_PASSWORD = 'fodvqpkwcryxoufg'
EMAIL_HOST_USER = 'rdeco1234.contact@gmail.com'
EMAIL_HOST_PASSWORD = 'bbppnmhigiafonqj'
EMAIL_USE_TLS = True

TIME_ZONE = 'Asia/Tokyo'
USE_TZ = False
