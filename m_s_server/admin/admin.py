from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from m_s_server.models.message import Message


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Message)

