import os
from django.shortcuts import redirect
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse

class DiscordAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Called on every social login. If the Discord user ID
        isn't whitelisted, immediately redirect to our unauthorized page.
        """
        uid = sociallogin.account.uid  # string
        allowed = os.getenv("ALLOWED_DISCORD_USER_IDS", "").split(",")
        if uid not in allowed:
            # Short‐circuit the flow and go to /accounts/profile/
            raise ImmediateHttpResponse(redirect("account_profile"))
        # Otherwise, continue as normal
        return super().pre_social_login(request, sociallogin)
