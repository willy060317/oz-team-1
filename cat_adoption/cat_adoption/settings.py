import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'X7k9p2mQ8vL3xY5zA1bC4dE6fG9hJ2iK5lM8nP0qR3sT6uW9vX2yZ4aB7cD0eF3g'  # 무작위 키로 대체하세요

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cat_adoption',
        'USER': 'cat_user',
        'PASSWORD': 'MySecurePass123!',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

S3 설정 (아직 키가 없으므로 주석 처리)
AWS_ACCESS_KEY_ID = 'REDACTED'  # 실제 AWS 액세스 키로 교체
AWS_SECRET_ACCESS_KEY = 'REDACTED'  # 실제 AWS 시크릿 키로 교체
AWS_STORAGE_BUCKET_NAME = 'cat-adoption-bucke'
AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cats',  # 사용자 정의 앱
    'storages',
    'rest_framework',  # REST API 지원
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # 세션 처리
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 인증 처리
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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

ROOT_URLCONF = 'cat_adoption.urls'
WSGI_APPLICATION = 'cat_adoption.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = '/static/'

# Media files (for file uploads, temporary use until S3 is set up)
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Add this to your urls.py for media serving in development
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [your_patterns_here] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)