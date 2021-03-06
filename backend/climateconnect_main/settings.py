"""
Django settings for climateconnect_main project.

Generated by 'django-admin startproject' using Django 2.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv('.backend_env'))
env = os.environ.get
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
# DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'api.climateconnect.earth'
]

AUTO_VERIFY = env('AUTO_VERIFY')

# Application definition

CUSTOM_APPS = [
    'climateconnect_api',
    'organization'
]

LIBRARY_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'knox',
    'corsheaders',
    'django_filters'
]

INSTALLED_APPS = CUSTOM_APPS + LIBRARY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://frontend-dot-inbound-lexicon-271522.ey.r.appspot.com",
    "https://alpha.climateconnect.earth",
    "https://climateconnect.earth",
    "https://www.climateconnect.earth"
]
APPEND_SLASH = False

ROOT_URLCONF = 'climateconnect_main.urls'

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

WSGI_APPLICATION = 'climateconnect_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT', '5432')
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
if(env('ENVIRONMENT') not in('development', 'test')):
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = env('GS_BUCKET_NAME')
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATIC_URL = '/static/' if env('ENVIRONMENT') in ('development', 'test') else 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)
STATIC_ROOT = env('STATIC_ROOT') if env('ENVIRONMENT') in ('development', 'test') else "static/"
MEDIA_ROOT = env('MEDIA_ROOT')
MEDIA_URL = '/media/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 200
}


SENDGRID_API_KEY = env('SENDGRID_API_KEY', '')
CLIMATE_CONNECT_SUPPORT_EMAIL = env('CLIMATE_CONNECT_SUPPORT_EMAIL', '')
SENDGRID_EMAIL_VERIFICATION_TEMPLATE_ID = env('SENDGRID_EMAIL_VERIFICATION_TEMPLATE_ID', '')
SENDGRID_NEW_EMAIL_VERIFICATION_TEMPLATE_ID = env('SENDGRID_NEW_EMAIL_VERIFICATION_TEMPLATE_ID', '')
SENDGRID_RESET_PASSWORD_TEMPLATE_ID = env('SENDGRID_RESET_PASSWORD_TEMPLATE_ID', '')
FRONTEND_URL = env('FRONTEND_URL', '')

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True
