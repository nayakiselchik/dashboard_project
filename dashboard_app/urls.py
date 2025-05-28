from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("click/<str:channel_id>/", views.ticket_click, name="ticket_click"),
    path("api/tickets/", views.ticket_status, name="ticket_status"),
]
