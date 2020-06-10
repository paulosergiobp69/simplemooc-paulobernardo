"""
Django settings for SimpleMooc project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q)yjfupa7tr0vpvkga5#l==m*d&^alkp_qa#rl1c4-nmf$(=2m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SimpleMooc.core',
    'SimpleMooc.accounts',
    'SimpleMooc.courses'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SimpleMooc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'SimpleMooc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'simplemooc', 'media')
MEDIA_URL  = '/media/'

# configuração para emvio de email pelo django, utilizando uma conta
# do gmail 
# E-mails
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'paulosergiobp@gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'email.gmail.com'
# EMAIL_HOST_PASSWORD = '@1k09981'
# EMAIL_PORT = 587

# para testes vamos mostrar no console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Nome email@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email.gmail.com'
EMAIL_HOST_PASSWORD = 'senha'
EMAIL_PORT = 587
#CONTACT_EMAIL = 'contato@simplemooc.com'
CONTACT_EMAIL = 'paulosergiobp@gmail.com'
"""
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'Nome paulosergiobp@gmail.com.br'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'paulosergiobp@gmail.com.br'
EMAIL_HOST_PASSWORD = 'm1gu3l@1969'
EMAIL_PORT = 587
CONTACT_EMAIL = 'paulosergiobp@gmail.com.br'
"""
# Autencicacao accounts
#LOGIN_URL = '/conta/entrar/'
#LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'accounts.login'
LOGIN_REDIRECT_URL = 'core.home'
LOGOUT_URL = 'accounts.logout'
AUTH_USER_MODEL = 'accounts.User'

# Heroku settings
import dj_database_url

DATABASES = {
    'default':  dj_database_url.config(),
}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


try:
    from SimpleMooc.local_settings import *
except ImportError:
    pass

