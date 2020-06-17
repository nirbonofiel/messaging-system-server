from django.contrib import admin
from django.contrib.auth import get_user_model

from m_s_server.admin.admin_models import UsersAdmin
from m_s_server.models.message import Message


admin.site.register(get_user_model(), UsersAdmin)
admin.site.register(Message)

