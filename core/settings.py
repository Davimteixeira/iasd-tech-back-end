import os
from pathlib import Path
from datetime import timedelta
from decouple import AutoConfig

BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = "accounts.User"  

config = AutoConfig(search_path=f"{BASE_DIR}/.env")

PROJECT_NAME = config("EcoMonitor", default="EcoMonitor")

SECRET_KEY = config("SECRET_KEY", default="S#perS3crEt_2387")

DEBUG = config("DEBUG", default=True, cast=bool)

TEST_MODE = config("TEST_MODE", default=False, cast=bool)

if TEST_MODE:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "http://0.0.0.0:4200",
    ]  
    CORS_ALLOW_ALL_ORIGINS = True  
    ALLOWED_HOSTS = ["*"]
else:
    CORS_ALLOWED_ORIGINS = config(
        "CORS_ALLOWED_ORIGINS",
        cast=lambda v: [s.strip() for s in v.split(",")],
        default=[
            "http://localhost:4200",
            "http://127.0.0.1:4200"
        ],
    )
    CORS_ALLOW_ALL_ORIGINS = False  

    ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default=[
        "localhost",
        "127.0.0.1",
        "0.0.0.0"
    ],
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',  
    'corsheaders',
    "apps.accounts",
    "apps.categories",
    "apps.products",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB_NAME"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASS"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
        "TEST": {
            'NAME': 'banco_de_testes_iasd',  
        },
    },
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
)

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

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Fortaleza"

USE_I18N = True

USE_TZ = False

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = "apps/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "USER_ID_FIELD": "id",
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_CLAIM": "id",
    "USER_AUTHENTICATION_RULE": (
        "rest_framework_simplejwt.authentication.default_user_authentication_rule"
    ),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

DJANGO_SETTINGS_MODULE = config("DJANGO_SETTINGS_MODULE")
