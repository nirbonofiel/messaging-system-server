from django.utils import timezone
from django.db import models
from m_s_server.models.user import User


class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_messages", null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receive_messages", null=True)
    body = models.CharField(max_length=400, blank=False)
    subject = models.CharField(max_length=255, blank=False)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.subject}'
