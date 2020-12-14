"""
Django settings for cosmos project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import secret_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_settings.secrets["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = secret_settings.secrets["DEBUG"]

# Pretix config
PRETIX_DOMAIN = secret_settings.secrets["PRETIX_DOMAIN"]
AUTHORIZATION_HEADER = secret_settings.secrets["PRETIX_AUTHORIZATION_HEADER"]

ALLOWED_HOSTS = secret_settings.secrets["ALLOWED_HOSTS"]

# Application definition


ROOT_URLCONF = "cosmos.urls"

WSGI_APPLICATION = "cosmos.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": secret_settings.secrets["DATABASES"]["DEFAULT"]["NAME"],
        "USER": secret_settings.secrets["DATABASES"]["DEFAULT"]["USER"],
        "PASSWORD": secret_settings.secrets["DATABASES"]["DEFAULT"]["PASSWORD"],
        "HOST": secret_settings.secrets["DATABASES"]["DEFAULT"]["HOST"],
        "PORT": secret_settings.secrets["DATABASES"]["DEFAULT"]["PORT"],
        "OPTIONS": secret_settings.secrets["DATABASES"]["DEFAULT"]["OPTIONS"],
    },
    "legacy": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": secret_settings.secrets["DATABASES"]["LEGACY"]["NAME"],
        "USER": secret_settings.secrets["DATABASES"]["LEGACY"]["USER"],
        "PASSWORD": secret_settings.secrets["DATABASES"]["LEGACY"]["PASSWORD"],
        "HOST": secret_settings.secrets["DATABASES"]["LEGACY"]["HOST"],
        "PORT": secret_settings.secrets["DATABASES"]["LEGACY"]["PORT"],
        "OPTIONS": secret_settings.secrets["DATABASES"]["LEGACY"]["OPTIONS"],
    },
}

DATABASE_ROUTERS = ["apps.legacy.legacy_router.LegacyRouter"]

SILENCED_SYSTEM_CHECKS = ["models.W035"]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, "media")
STATIC_ROOT = os.path.join(DATA_DIR, "static")

STATICFILES_STORAGE = "pipeline.storage.PipelineManifestStorage"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
]

PIPELINE = {
    "CSS_COMPRESSOR": "pipeline.compressors.yuglify.YuglifyCompressor",
    "YUGLIFY_BINARY": "node_modules/.bin/yuglify",
    "JS_COMPRESSOR": "pipeline.compressors.closure.ClosureCompressor",
    "CLOSURE_BINARY": "node_modules/.bin/google-closure-compiler",
    "STYLESHEETS": {
        "cosmos": {
            "source_filenames": {"cosmos/css/registration.css", "cosmos/css/core.css"},
            "output_filename": "cosmos/css/cosmos.css",
        },
        "cosmos_cms": {
            "source_filenames": {
                "cosmos_cms/css/board_list.css",
                "cosmos_cms/css/board_title.css",
                "cosmos_cms/css/committee_list.css",
                "cosmos_cms/css/committee_title.css",
            },
            "output_filename": "cosmos_cms/css/cosmos_cms.css",
        },
    },
    "JAVASCRIPT": {
        "cosmos": {
            "source_filenames": {
                "cosmos/js/sidebar.js",
                "cosmos/js/register.js",
                "cosmos/js/profile.js",
            },
            "output_filename": "cosmos/js/cosmos.js",
        },
    },
}

SITE_ID = 1

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "cosmos", "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
                "sekizai.context_processors.sekizai",
                "django.template.context_processors.static",
                "cms.context_processors.cms_settings",
            ],
            "loaders": ["django.template.loaders.filesystem.Loader", "django.template.loaders.app_directories.Loader"],
        },
    },
]

MIDDLEWARE = [
    "cms.middleware.utils.ApphookReloadMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

INSTALLED_APPS = [
    "cosmos",
    "apps.users",
    "apps.legacy",
    "apps.cms_plugins",
    "apps.events",
    "djangocms_admin_style",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "cms",
    "menus",
    "sekizai",
    "treebeard",
    "djangocms_text_ckeditor",
    "filer",
    "easy_thumbnails",
    "djangocms_file",
    "djangocms_icon",
    "djangocms_link",
    "djangocms_picture",
    "djangocms_style",
    "djangocms_snippet",
    "djangocms_googlemap",
    "djangocms_video",
    "django_better_admin_arrayfield",
    "pipeline",
    "django_celery_results",
]

LANGUAGES = (
    # Customize this
    ("en", "en"),
)

CMS_LANGUAGES = {
    # Customize this
    1: [{"code": "en", "name": "en", "redirect_on_fallback": True, "public": True, "hide_untranslated": False}],
    "default": {"redirect_on_fallback": True, "public": True, "hide_untranslated": False},
}

CMS_TEMPLATES = (
    # Customize this
    ("fullwidth.html", "Fullwidth"),
    ("sidebar_left.html", "Sidebar Left"),
    ("sidebar_right.html", "Sidebar Right"),
)

X_FRAME_OPTIONS = "SAMEORIGIN"

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# Logging
# https://docs.djangoproject.com/en/3.1/topics/logging/
LOGGING_FOLDER = secret_settings.secrets["LOGGING"]["FOLDER"]  # relative to root of project
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        # copied from DEFAULT_LOGGING https://github.com/django/django/blob/master/django/utils/log.py
        "verbose": {"()": "django.utils.log.ServerFormatter", "format": "[{server_time}] {message}", "style": "{"}
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "filters": ["require_debug_true"], "formatter": "verbose"},
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "filename": os.path.join(LOGGING_FOLDER, "debug.log"),
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console", "mail_admins"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# Email
# https://docs.djangoproject.com/en/3.1/topics/email/

EMAIL_HOST = secret_settings.secrets["EMAIL"]["HOST"]
EMAIL_PORT = secret_settings.secrets["EMAIL"]["PORT"]
EMAIL_HOST_USER = secret_settings.secrets["EMAIL"]["USERNAME"]
EMAIL_HOST_PASSWORD = secret_settings.secrets["EMAIL"]["PASSWORD"]
EMAIL_USE_TLS = secret_settings.secrets["EMAIL"]["USE_TLS"]

# TODO Always set default to noreply
DEFAULT_FROM_EMAIL = secret_settings.secrets["EMAIL"]["USERNAME"]

LOGOUT_REDIRECT_URL = "/"

# Security

SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

SECURE_REFERRER_POLICY = "same-origin"

# Celery
CELERY_BROKER_URL = "amqp://guest:guest@localhost//"
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
