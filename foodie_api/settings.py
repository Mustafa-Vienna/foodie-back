from pathlib import Path
import os
import dj_database_url
from datetime import timedelta

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
if os.path.exists("env.py"):
    exec(open("env.py").read())

# SECURITY SETTINGS
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is not set")

DEBUG = os.getenv("DEV") == "1"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# CORS & CSRF SETTINGS
CSRF_TRUSTED_ORIGINS = [os.getenv("CLIENT_ORIGIN", "http://localhost:3000")]
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Lax"

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS") == "1"
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://foodiefront-bac5250c6d8.herokuapp.com",
    ]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https:\/\/.*\.codeinstitute-ide\.net$",
]

# Ensure proper CORS settings
if "CLIENT_ORIGIN" in os.environ:
    CORS_ALLOWED_ORIGINS.append(os.getenv("CLIENT_ORIGIN"))

# Ensure Cloudinary settings exist
if "CLOUDINARY_URL" not in os.environ:
    raise ValueError("CLOUDINARY_URL environment variable is not set")

# Cloudinary Configuration
CLOUDINARY_STORAGE = {
    "CLOUDINARY_URL": os.getenv("CLOUDINARY_URL")
}
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATIC & MEDIA FILES
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DATETIME_FORMAT": "%a, %d %b %Y %H:%M:%S",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

if os.getenv("DEV") != "1":
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
        "rest_framework.renderers.JSONRenderer",
    ]

# JWT Authentication Settings
REST_USE_JWT = True
TOKEN_MODEL = None
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

JWT_AUTH_COOKIE = "jwt-access-token"
JWT_AUTH_REFRESH_COOKIE = "jwt-refresh-token"
JWT_AUTH_SAMESITE = "Lax"
JWT_AUTH_SECURE = os.getenv("JWT_AUTH_SECURE") == "1"
JWT_AUTH_HTTPONLY = True

# ACCOUNT SETTINGS
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_VERIFICATION = os.getenv("ACCOUNT_EMAIL_VERIFICATION", "none")

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "foodie_api.serializers.CustomRegisterSerializer"
}

# APPLICATIONS
INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary_storage",
    "cloudinary",
    "rest_framework",
    "django_filters",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "rest_framework_simplejwt",
    "django_extensions",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "profiles",
    "posts",
    "comments",
    "likes",
    "followers",
]

SITE_ID = 1

# MIDDLEWARE CONFIGURATION
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# URLS AND WSGI SETTINGS
ROOT_URLCONF = "foodie_api.urls"
WSGI_APPLICATION = "foodie_api.wsgi.application"

# TEMPLATE SETTINGS
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

# DATABASE CONFIGURATION
DATABASES = { "default": dj_database_url.parse(os.getenv("DATABASE_URL")) }

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
