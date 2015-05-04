import os
from django.core.urlresolvers import reverse_lazy
import dj_database_url

# Our django-pipeline settings
PATH_TO_HERE = os.getcwd()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'vvj&+a94!^+aa%2ghr#!2o*)kzn)bnl4m*!6zrab3(a2$l)!^0'
DEBUG = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Miscellaneous
SITE_ID = 1
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('cowork:dashboard')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cowork',
)

GENERIC_APPS = (
    'authtools',
    'pipeline',
)

LOCAL_APPS = (
    'accounts',

)

INSTALLED_APPS += LOCAL_APPS + GENERIC_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'coworkok.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'coworkok', 'templates'),
        ],
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

WSGI_APPLICATION = 'coworkok.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] =dj_database_url.config()
# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


# Django Pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE = True
PIPELINE_AUTO = True
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS = {
    'dashboard': {
        'source_filenames': (
            'static/cowork/less/dashboard.less',
        ),
        'output_filename': 'static/cowork/less/dashboard.css'
    },
    'accounts': {
        'source_filenames': (
            'static/accounts/less/accounts.less',
        ),
        'output_filename': 'static/accounts/less/accounts.css'
    }
}
# If we are on heroku we want to re-define the location of the less binary.
HEROKU_LESSC = os.path.join(PATH_TO_HERE, 'lib/node_modules/less/bin/lessc')
HEROKU_NODE = os.path.join(PATH_TO_HERE, 'bin/node')
if os.path.exists(HEROKU_LESSC):
    PIPELINE_LESS_BINARY = "{0} {1}".format(HEROKU_NODE, HEROKU_LESSC)

PIPELINE_LESS_ARGUMENTS = '--include-path=' + ':'.join('{0}/{1}/static/less'.format(PATH_TO_HERE, app) for app in INSTALLED_APPS if app in os.listdir(PATH_TO_HERE))
