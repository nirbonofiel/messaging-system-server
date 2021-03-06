from rest_framework import serializers
from django.contrib.auth import get_user_model

user_model = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = user_model
        fields = ['id', 'username', 'full_name']


