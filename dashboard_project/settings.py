import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INSTALLED_APPS = [
    # core Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # your app
    "dashboard_app",

    # allauth for Discord OAuth2
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.discord",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "dashboard_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "dashboard_app" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # <— needed by allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dashboard_project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "dashboard_app" / "static"]

# Authentication configuration
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# 1) Redirect anonymous users trying to hit @login_required views here
LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"
ACCOUNT_LOGOUT_ON_GET = True

# 2) Allauth: Discord only, no local signups
ACCOUNT_ALLOW_REGISTRATION = False
SOCIALACCOUNT_AUTO_SIGNUP  = True   # <-- auto-create whitelisted users
ACCOUNT_EMAIL_REQUIRED     = False
ACCOUNT_EMAIL_VERIFICATION = "none"

# 3) Skip the “Confirm sign in via Discord” page
SOCIALACCOUNT_LOGIN_ON_GET  = True

# 4) Use your adapter to enforce whitelist
SOCIALACCOUNT_ADAPTER = "dashboard_app.adapter.DiscordAccountAdapter"

# 5) Discord OAuth2 credentials & scopes
SOCIALACCOUNT_PROVIDERS = {
    "discord": {
        "APP": {
            "client_id": os.getenv("DISCORD_OAUTH_CLIENT_ID"),
            "secret": os.getenv("DISCORD_OAUTH_CLIENT_SECRET"),
            "key": "",
        },
        "SCOPE": ["identify", "guilds"],
    }
}
