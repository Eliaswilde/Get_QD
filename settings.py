# Global settings for getqd_2014 project.
import os, sys

PROJECT_DIR = os.path.dirname(__file__)
ADMINS = (
    ('Den Rybin', 'Denrybin891016@mail.com'),
)
MANAGERS = ADMINS

# Enviroment
SITE_ID = 1
DEBUG = False
TEMPLATE_DEBUG = True

# Paths
sys.path.insert(0, os.path.join(PROJECT_DIR, "apps"))

ALLOWED_HOSTS = ['*']

# User uploaded files
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Static
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'apps', 'main', 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Other django settings
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
ROOT_URLCONF = 'urls'
# WSGI_APPLICATION = 'conf.wsgi.application'



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
     # third party
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
     # locale
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # third party
    'allauth', 'allauth.account', 'allauth.socialaccount',
    'south', 'rest_framework', 'compressor', 'activelink',
    # locale
    'main'
)

# ALLAUTH settings
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'SCOPE': ['email', 'publish_stream'],
#         'METHOD': 'js_sdk'  # instead of 'oauth2'
#     }
# }

# compressor
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/less', '/usr/bin/lessc {infile}'),
)
COMPRESS_ROOT = os.path.join(PROJECT_DIR, 'static')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        pass
