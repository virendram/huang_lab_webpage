"""
Django settings for huang_webpage project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from  .email_info import *
# This is for gmail
EMAIL_USE_TLS=EMAIL_USE_TLS
EMAIL_HOST=EMAIL_HOST
EMAIL_HOST_USER=EMAIL_HOST_USER
EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD
EMAIL_PORT=EMAIL_PORT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')h*up2ky!+000^f4m+jf50ri8a14+b!*vwz)uuc@cp!s+r5)8n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Set to False when deploying -- Virendra

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [] # Change to brainmrimaps.org later -- Virendra


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'signups',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'huang_webpage.urls'

WSGI_APPLICATION = 'huang_webpage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Template location
TEMPLATE_DIRS=(
    os.path.join(os.path.dirname(BASE_DIR),"static_directory","templates"),
)

if DEBUG:
    MEDIA_URL='/media/'
    STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_directory","static-only")
    MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_directory","media")
    STATICFILES_DIRS=(
        os.path.join(os.path.dirname(BASE_DIR),"static_directory","static"),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)
#AUTHENTICATION_BACKENDS = ('django.contrib.auth.models.AbstractBaseUser',)
#AUTHENTICATION_BACKENDS = ( 'path.to.your.MyCustomBackend', )