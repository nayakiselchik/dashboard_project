from django.db import models

class Ticket(models.Model):
    channel_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=100)
    has_unread = models.BooleanField(default=False)

    def __str__(self):
        return self.name
