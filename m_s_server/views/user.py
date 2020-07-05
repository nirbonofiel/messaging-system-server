from rest_framework import generics, status
from m_s_server.services import user as user_service
from m_s_server.serializers import user as user_serializer
from rest_framework import permissions
from rest_framework.response import Response


class UserListApi(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = user_serializer.UserSerializer

    def get_queryset(self):
        queryset = user_service.get_all_users()
        return queryset


class UserMeApi(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK, data=user_serializer.UserSerializer(request.user).data)


user_list_api = UserListApi.as_view()
user_me_api = UserMeApi.as_view()
