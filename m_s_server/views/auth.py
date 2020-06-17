from django.contrib.auth import get_user_model
from rest_framework import views
from rest_framework.response import Response

user_model = get_user_model()


class Logout(views.APIView):

    def post(self, request, *args, **kwargs):
        return Response('logged out')


logout = Logout.as_view()
