from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model


user_model = get_user_model()


class UsersAdmin(ModelAdmin):
    model = user_model
