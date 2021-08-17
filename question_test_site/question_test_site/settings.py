
"""
Django settings for question_test_site project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


with open(BASE_DIR/'secret_key.txt') as f:
    SECRET_KEY = f.read().strip()


# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY =

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
    'rangefilter',
    'django_celery_results',
    "django_celery_beat",
    'rest_framework',
    'crispy_forms',
    'drf_yasg',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'django_filters',
    'channels'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# ASGI
ASGI_APPLICATION = 'question_test_site.asgi.application'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'question_test_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'question_test_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validarest_framework_simplejwt.authentication.JWTAuthentication'tion
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = [
    ('en', 'English'),
    ('uk', 'Ukrainian'),
]

from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Kiev'
CELERY_BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BEAT_SCHEDULE = {
    'create-report-every-day': {
        'task': 'polls.tasks.create_log',
        'schedule': crontab(hour=20, minute=00),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = [
    '127.0.0.1',
]

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

U_LOGFILE_SIZE = 5 * 1024 * 1024
U_LOGFILE_COUNT = 0
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'actions': {
#             'format': '%(asctime)s [%(levelname)s]::: %(name)s: %(message)s'
#         },
#         'actions_timeout': {
#             'format': '%(asctime)s [%(levelname)s]::: %(name)s: %(message)s'
#         },
#         'console': {
#             'format': '%(asctime)s [%(levelname)s]::: %(name)s: %(message)s'
#         },
#     },
#     'handlers': {
#         'actions': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(LOGGING_DIR, 'actions.log'),
#             'maxBytes': U_LOGFILE_SIZE,
#             'backupCount': U_LOGFILE_COUNT,
#             'formatter': 'actions',
#         },
#         'actions_timeout': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#
#             'when': 'midnight',
#             'interval': 1,
#             'filename': os.path.join(LOGGING_DIR, 'actions.log'),
#             'formatter': 'actions_timeout',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'console',
#         },
#     },
#     'loggers': {
#         'tests_app': {
#             'handlers': ['actions', 'console', 'actions_timeout'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django': {
#             'handlers': ['actions', 'actions_timeout'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#             'propagate': False,
#         },
#         'django.request': {
#             'handlers': ['actions', 'actions_timeout'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#             'propagate': False,
#         },
#     },
# }

# DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': "%Y/%m/%d %H:%M:%S",
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
# SESSIONS_ENGINE = 'django.contrib.sessions.backends.cache'
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': '127.0.0.1:11211',
#         'TIMEOUT': 3600,
#     }
# }
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': [
           '127.0.0.1:11211',
        ],
    }
}

# Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}


# Additional middleware

