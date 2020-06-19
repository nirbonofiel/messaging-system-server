from django.contrib.auth import get_user_model

user_model = get_user_model()


def get_user(username, password):
    return user_model.object.get(username=username, password=password)


def get_all_users():
    return user_model.objects.all()
