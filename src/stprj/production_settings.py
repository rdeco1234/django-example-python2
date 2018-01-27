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
)

STATIC_URL = '/static/'
STATIC_ROOT = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs/static'

#TEMPLATE_DIR = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs/rdeco_hp'
TEMPLATE_DIR = '/home/rdeco/www/rdeco.sakura.ne.jp/htdocs'

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
    'version': 1,   # ��������ꤷ�ʤ����ܤ���
    'formatters': { # ���ϥե����ޥåȤ�ʸ��������ǻ��ꤹ��
        'all': {    # ���ϥե����ޥåȤ�`all`�Ȥ���̾����Ĥ���
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
    'handlers': {  # ����ɤ��˽Ф���������
        'file': {  # �ɤ��˽Ф����������̾����Ĥ��� `file`�Ȥ���̾����Ĥ��Ƥ���
            'level': 'DEBUG',  # DEBUG�ʾ�Υ����갷���Ȥ�����̣
            'class': 'logging.FileHandler',  # ������Ϥ��뤿��Υ��饹�����
            'filename': os.path.join(BASE_DIR, 'django.log'),  # �ɤ��˽Ф���
            'formatter': 'all',  # �ɤν��ϥե����ޥåȤǽФ�����̾���ǻ���
        },
        'console': { # �ɤ��˽Ф����������⤦��ġ������������ˤ�`console`�Ȥ���̾��
            'level': 'DEBUG',
            # �������ɸ����Ϥ˽Ф��Ƥ���륯�饹�����
            'class': 'logging.StreamHandler', 
            'formatter': 'all'
        },
    },
    'loggers': {  # �ɤ��logger�����뤫�����ꤹ��
        'command': {  # command�Ȥ���̾����logger�����
            'handlers': ['file', 'console'],  # ��Ҥ�file, console������ǽ���
            'level': 'DEBUG',
        },
    },
}
