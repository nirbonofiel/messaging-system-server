from rest_framework import serializers
from m_s_server.models.message import Message

from m_s_server.utils.timestamp_field import TimestampField


class MessageSerializer(serializers.ModelSerializer):

    creation_date = TimestampField(required=False)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'body', 'subject', 'creation_date']

