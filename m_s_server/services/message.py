from m_s_server.models.message import Message


def get_all_messages():
    return Message.objects.all()


def get_messages_by_receiver(receiver):
    return Message.objects.filter(receiver=receiver)
