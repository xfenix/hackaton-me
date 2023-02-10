"""Django settings for my_project project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

from envparse import env as envparse


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v_44o1ikx2_r%jv-kfqg92mocmnmi)i*wbbf=5!kx$!*^*_0zd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = envparse("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'cashapp',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'my_project', 'templates')],
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

WSGI_APPLICATION = 'my_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'raiff2023-1',
            'USER': 'raiff2023-1',
            'HOST': 'https://rc1b-eyos84hkn45bnqei.mdb.yandexcloud.net',
            'PORT': '6432',
        }
    }

# psql "host=rc1b-eyos84hkn45bnqei.mdb.yandexcloud.net \
#       port=6432 \
#       sslmode=verify-full \
#       dbname=raiff2023-1 \
#       user=raiff2023-1 \
#       target_session_attrs=read-write"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APP_URL_BASE: str = envparse('APP_URL', 'https://self-service-checkout-events.5723.raiff2023.codenrock.com').rstrip("/")
REDIRECT_URL: str = envparse('PAYMENT_REDIRECT_URL', 'order', cast=str).strip('/')
QR_GENERATION_URL: str = envparse('RAIFFEISEN_SBP_URL', 'https://pay-test.raif.ru/api/sbp/v2/qrs', cast=str).rstrip("/")
QR_CODE_BOX_SIZE: int = envparse("QR_CODE_BOX_SIZE", default=40, cast=int)
QR_TYPE: str = envparse('QR_CODE_TYPE', 'QRDynamic', cast=str)
CHECKOUT_INFIX: str = envparse('CHECKOUT_INFIX', 'checkout', cast=str)
CURRENCY: str = envparse('CURRENCY', 'RUB', cast=str)

BACKGROUND_CHOICES: tuple[str, ...] = ('orchestra', 'conference', 'museum', 'party2', 'party1')
LOGO_CHOICES: tuple[str, ...] = ('16tonn', 'ontico', 'satirikon', 'pycon')

CORS_ALLOW_ALL_ORIGINS: bool = True

SMS_LOGIN: str = envparse('SMS_LOGIN', 'xfenix', cast=str)
SMS_PASSWORD: str = envparse('SMS_PASSWORD', 'GachiEtoHorosho123', cast=str)
