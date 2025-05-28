#!/usr/bin/env python
import os, sys
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard_project.settings")

# ensure Django is bootstrapped
import django
django.setup()

from dashboard_app.models import Ticket
from asgiref.sync import sync_to_async
import discord

TOKEN       = os.getenv("DISCORD_TOKEN")
GUILD_ID    = int(os.getenv("DISCORD_GUILD_ID"))
CHANNEL_IDS = [int(x) for x in os.getenv("DISCORD_CHANNEL_IDS", "").split(",") if x]

intents = discord.Intents.default()
intents.messages = True

class TicketBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)

    async def on_ready(self):
        guild = self.get_guild(GUILD_ID)
        # ensure rows for each channel
        for cid in CHANNEL_IDS:
            await sync_to_async(Ticket.objects.get_or_create)(
                channel_id=str(cid),
                defaults={"name": guild.get_channel(cid).name},
            )
        print("Bot ready.")

    async def on_message(self, message):
        if message.guild and message.guild.id == GUILD_ID:
            cid = str(message.channel.id)
            if cid in map(str, CHANNEL_IDS):
                t = await sync_to_async(Ticket.objects.get)(channel_id=cid)
                t.has_unread = True
                await sync_to_async(t.save)()
                print(f"Marked {t.name} unread.")

def main():
    TicketBot().run(TOKEN)

if __name__ == "__main__":
    main()
