"""
Django settings for pillarplus project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from corsheaders.defaults import default_headers
import os
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    JWT_SECRET =(str,'.ZOPW9{c~T4M?Btn_nf4h\]CYs@"6*=WQw5}OxV\}'),
    SERVER_URL =(str,'http://127.0.0.1:8000'),
    TOKEN_TIMELINE =(int,1),
    REFRESH_TOKEN_TIMELINE =(int,1),
)
environ.Env.read_env(os.path.join(BASE_DIR, 'pillarplus/.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hcqp#t_(z!g+tx3^7@_1yj6fu(@-nunrdc=!%lb#aiax9e)z@k'

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

     # installed app
    'rest_framework',
    'corsheaders',
    'drf_yasg',

    #created app
    "user.apps.UserConfig",
    "user_form.apps.UserFormConfig",
    "master_file",
    "helper",
    'custom_middelware',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'custom_middelware.Auth.AuthMiddleware',
]

ROOT_URLCONF = 'pillarplus.urls'

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

WSGI_APPLICATION = 'pillarplus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASE_NAME = '************************'
DATABASE_HOST = 'localhost'
PORT = '27017'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': DATABASE_NAME,
        'HOST': DATABASE_HOST,
        'PORT': PORT
    }
}

# Password validation
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

AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ********************* SWAGGER SETTING ***************************

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'JSON_EDITOR': True,
}

# **********************************************************************

# ******************** REST FRAMEWORK SETTING **************************


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

# ***********************************************************************

# ************************CORS HEADER SETTING******************************

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    "token","rtoken"
]

CORS_EXPOSE_HEADERS = ["token","rtoken"]

#*******************************************************************************

JWT_SECRET = env('JWT_SECRET')
TOKEN_TIMELINE = env('TOKEN_TIMELINE')
REFRESH_TOKEN_TIMELINE = env('REFRESH_TOKEN_TIMELINE')
SERVER_URL = env('SERVER_URL')

if not os.path.isdir(f'{BASE_DIR}\media'):
    os.mkdir(f'{BASE_DIR}\media')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
