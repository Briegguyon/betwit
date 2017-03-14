"""
Django settings for betwit project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6!+bpsae@makhnh^fkji0d2c2(n2#m3=jv(&5k)^y91%5ar1m3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'jquery',
    'bets',
    'tournaments',
    'registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'bets.middleware.TimezoneMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'betwit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join( BASE_DIR, 'templates' )],
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

WSGI_APPLICATION = 'betwit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'console': {
#            'class': 'logging.StreamHandler',
#        },
#    },
#    'loggers': {
#        'django': {
#            'handlers': ['console'],
#            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#        },
#    },
#}
# http://thegeorgeous.com/2015/02/27/Logging-into-multiple-files-in-Django.html
# https://www.webforefront.com/django/setupdjangologging.html
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # filters will define when a logger should run
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # format in which logs will be written
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    # handlers define the file to be written, which level to write in that file,
    # which format to use and which filter applies to that logger
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'development_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'log/django_dev.log',
            'formatter': 'verbose'
        },
        'production_logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'log/django_production.log',
            'formatter': 'simple'
        },
        'dba_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_false','require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'log/django_dba.log',
            'formatter': 'simple'
        },
    },
    # here the handlers for the loggers and the level of each logger is defined
    'loggers': {
        'bets': {
            'handlers': ['console','development_logfile','production_logfile'],
         },
         'tournaments': {
            'handlers': ['console','development_logfile','production_logfile'],
         },
        'dba': {
            'handlers': ['console','dba_logfile'],
        },
        'django': {
            'handlers': ['console','development_logfile','production_logfile'],
        },
        'py.warnings': {
            'handlers': ['console','development_logfile'],
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
IMAGE_UPLOAD_PATH = os.path.join(STATIC_ROOT, 'uploadsImg')
THUMBNAIL_UPLOAD_PATH = os.path.join(STATIC_ROOT, 'thumbnails')
# Simplified static file serving.
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = '/bets/u/'
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
REGISTRATION_AUTO_LOGIN = False # Automatically log the user in.

# smtpout=
# send email in console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
