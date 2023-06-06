"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import json
import os
from platform import system as sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY
SECRET_DIR = BASE_DIR / ".secrets"
secrets = json.load(open(os.path.join(SECRET_DIR, "secret.json")))
SECRET_KEY = secrets["DJANGO_SECRET_KEY"]

# MEDIA 경로
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# TEMPLATE 경로
TEMPLATE_DIR = BASE_DIR / "templates"

# Debug, Allowed_hosts settings based on development environment
LOCAL = True if sys().lower().startswith("darwin") or sys().lower().startswith("windows") else False

# STATIC 경로
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [BASE_DIR / "static"]


# SECURITY WARNING: don't run with debug turned on in production!
if LOCAL:
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
else:
    DEBUG = False
    ALLOWED_HOSTS = [
        "127.0.0.1", 
        secrets["CSRF_TRUSTED_ORIGINS"]["AWS_LAMBDA"], 
        secrets["CSRF_TRUSTED_ORIGINS"]["DOMAIN"]
    ]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "board"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },  
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


DATABASES = {
    "default": {
        "NAME": secrets["RDS_MySQL"]["DB_NAME"],
        "ENGINE": "django.db.backends.mysql",
        "USER": secrets["RDS_MySQL"]["DB_USER"],
        "PASSWORD": secrets["RDS_MySQL"]["DB_PASS"],
        "HOST": secrets["RDS_MySQL"]["DB_HOST"],
        "PORT": "3306",
        "OPTIONS": {
            "autocommit": True,
            "charset": "utf8mb4",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_TRUSTED_ORIGINS = [
    secrets["CSRF_TRUSTED_ORIGINS"]["NGROK_URL"],
    secrets["CSRF_TRUSTED_ORIGINS"]["AWS_LAMBDA"],
    secrets["CSRF_TRUSTED_ORIGINS"]["DOMAIN"],
]


# AWS S3 설정
AWS_ACCESS_KEY_ID = secrets["S3"]["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = secrets["S3"]["AWS_SECRET_ACCESS_KEY"]
AWS_REGION = secrets["S3"]["AWS_S3_REGION_NAME"]
AWS_STORAGE_BUCKET_NAME = secrets["S3"]["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com"
AWS_DEFAULT_ACL = "public-read"
DEFAULT_FILE_STORAGE = "config.storages.S3DefaultStorage"
STATICFILES_STORAGE = "config.storages.S3StaticStorage"