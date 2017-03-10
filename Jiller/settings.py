import os

from kombu import Exchange, Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta
from redislite import Redis

from django.urls.base import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)

MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

MEDIA_URL = '/media/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'olj^%!kemjn61dic)!y3k!(51&vciz$2jf*w_mji-(f(nwz#7$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from socket import gethostname

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', gethostname(),
                 os.environ.get('OPENSHIFT_APP_DNS')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'project',
    'employee',
    'general',
    'sorl.thumbnail',
    'django_nose',
    'waffle',
    'simple_email_confirmation',
    'django_tables2',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'mathfilters',
]

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'waffle.middleware.WaffleMiddleware',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Jiller.middleware.LoginRequiredMiddleware.LoginRequiredMiddleware',
    'Jiller.middleware.CheckProjectRelationMiddleware.CheckProjectRelation',
    'Jiller.middleware.SetLastSeenMiddleware.SetLastSeenMiddleware',
    'Jiller.middleware.SaveLastProjectMiddleware.SaveLastProjectMiddleware',
]

ROOT_URLCONF = 'Jiller.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Jiller.context_processors.project_list'
            ],
            'debug': True,
        },
    },
]

WSGI_APPLICATION = 'Jiller.wsgi.application'

LOGIN_REDIRECT_URL = reverse_lazy('general:home_page')
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join('../static')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


AUTH_USER_MODEL = 'employee.Employee'

LOGIN_URL = 'general:login'

LOGIN_EXEMPT_URLS = (

 r'^login/$',
 r'^registration/$',
 r'^confirmation/(?P<username>[a-zA-Z0-9]+)/(?P<key>[a-zA-Z0-9]+)/$',
 r'^sender/(?P<username>[a-zA-Z0-9]+)/$',
 r'^accounts/github/login/$',
 r'^accounts/twitter/login/$',
 r'^accounts/vk/login/$',
 r'^accounts/google/login/$',
 r'^accounts/linkedin/login/$',
 # need for edit social accounts in user profile
 r'^accounts/social/connections/$',
 r'^accounts/twitter/login/callback/$',
 r'^accounts/facebook/login/$',
 r'^accounts/instagram/login',
)



SOCIALACCOUNT_PROVIDERS = \
    {'linkedin':
         {'SCOPE': ['r_emailaddress']},
    'facebook':
        {'METHOD': 'oauth2',
         'SCOPE': ['email'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'LOCALE_FUNC': lambda request: 'en_US',
         'VERSION': 'v2.4'},
    'vk':
         {'SCOPE':['email'],
          'FIELDS': [
              'id',
              'email',
              'name',
              'first_name',
              'last_name'
          ],
          'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
          'METHOD':'oauth2',
          }
     }

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=general,project,employee',
]

PAGINATION_PER_PAGE = 20
LAST_ACTIVITY_INTERVAL_SECS = 900 # 15 min

try:
    from .local_settings import *
except ImportError:
    pass

# CELERY

# REDIS_DB_PATH = os.path.join(DATA_DIR,'my_redis.db')
# rdb = Redis(REDIS_DB_PATH, serverconfig={'port': '1116'})
# REDIS_SOCKET_PATH = 'redis+socket://%s' % (rdb.socket_file, )
# BROKER_URL = REDIS_SOCKET_PATH
# CELERY_RESULT_BACKEND = REDIS_SOCKET_PATH
#
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_IMPORTS = ['general.tasks']
# CELERY_TIMEZONE = 'UTC'

# Redis

REDIS_PORT = 6379
REDIS_DB = 0
REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', 'redis')

RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', 'rabbit')

if RABBIT_HOSTNAME.startswith('tcp://'):
    RABBIT_HOSTNAME = RABBIT_HOSTNAME.split('//')[1]

BROKER_URL = os.environ.get('BROKER_URL',
                            '')
if not BROKER_URL:
    BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}/'.format(
        user=os.environ.get('RABBIT_ENV_USER', 'admin'),
        password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'mypass'),
        hostname=RABBIT_HOSTNAME,
        vhost=os.environ.get('RABBIT_ENV_VHOST', ''))

# We don't want to have dead connections stored on rabbitmq, so we have to negotiate using heartbeats
BROKER_HEARTBEAT = '?heartbeat=30'
if not BROKER_URL.endswith(BROKER_HEARTBEAT):
    BROKER_URL += BROKER_HEARTBEAT

BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_TIMEOUT = 10

# Celery configuration

# configure queues, currently we have only one
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

# Sensible settings for celery
CELERY_ALWAYS_EAGER = False
CELERY_ACKS_LATE = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_DISABLE_RATE_LIMITS = False

# By default we will ignore result
# If you want to see results and try out tasks interactively, change it to False
# Or change this setting on tasks level
CELERY_IGNORE_RESULT = True
CELERY_SEND_TASK_ERROR_EMAILS = False
CELERY_TASK_RESULT_EXPIRES = 600

# Set redis as celery result backend
CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
CELERY_REDIS_MAX_CONNECTIONS = 1

# Don't use pickle as serializer, json is much safer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['application/json']

CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1000

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email.assign.python.webui@gmail.com'
EMAIL_HOST_PASSWORD = 'Kh004Python'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'email.assign.python.webui@gmail.com'

JILLER_HOST = 'http://jiller-phobosprogrammer.rhcloud.com'

