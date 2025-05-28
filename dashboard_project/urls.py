from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect
from dashboard_app import views as dash_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Block "/accounts/signup/" and send to the Discord login flow
    path("accounts/signup/", lambda req: redirect("account_login")),

    # Custom unauthorized page (whitelist failures go here)
    path("accounts/profile/", dash_views.unauthorized, name="account_profile"),

    # All the allauth URLs for login/logout, OAuth, etc.
    path("accounts/", include("allauth.urls")),

    # Now include your app’s URL patterns:
    # - "" → dashboard
    # - "click/<channel_id>/" → ticket_click
    # - "api/tickets/" → ticket_status
    path("", include("dashboard_app.urls")),
]

# In DEBUG only, serve static files from STATICFILES_DIRS
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
