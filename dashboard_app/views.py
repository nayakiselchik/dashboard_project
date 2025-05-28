import os
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Ticket

GUILD_ID = os.getenv("DISCORD_GUILD_ID")

@login_required(login_url='account_login')
def dashboard(request):
    tickets = Ticket.objects.all().order_by("name")
    return render(request, "dashboard.html", {
        "tickets": tickets,
        "guild_id": GUILD_ID,
    })

@login_required(login_url='account_login')
def ticket_click(request, channel_id):
    ticket = get_object_or_404(Ticket, channel_id=channel_id)
    ticket.has_unread = False
    ticket.save()
    return render(request, "redirect_to_discord.html", {
        "app_url": f"discord://-/channels/{GUILD_ID}/{channel_id}",
        "web_url": f"https://discord.com/channels/{GUILD_ID}/{channel_id}",
    })

@login_required(login_url='account_login')
def ticket_status(request):
    data = list(Ticket.objects.values("channel_id", "has_unread"))
    return JsonResponse({"tickets": data})

def unauthorized(request):
    return render(request, "account/unauthorized.html", status=403)
