from rest_framework import serializers
from m_s_server.models.message import Message
from m_s_server.serializers.user import UserSerializer

from m_s_server.utils.timestamp_field import TimestampField


class MessageFullSerializer(serializers.ModelSerializer):

    sender = UserSerializer()
    receiver = UserSerializer()
    creation_date = TimestampField(required=False)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'body', 'subject', 'creation_date']


class MessageSerializer(serializers.ModelSerializer):

    creation_date = TimestampField(required=False)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'body', 'subject', 'creation_date']

