from m_s_server.models.message import Message
from django.db.models import Q


def get_all_messages():
    return Message.objects.all()


def get_user_messages(user_id):
    return Message.objects.filter(Q(sender=user_id) | Q(receiver=user_id))
