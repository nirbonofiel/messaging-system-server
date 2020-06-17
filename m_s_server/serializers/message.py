from rest_framework import serializers
from m_s_server.models.message import Message
from m_s_server.serializers.user import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    # receiver = UserSerializer()
    # sender = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'body', 'subject', 'creation_date']

