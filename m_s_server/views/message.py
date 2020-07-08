from rest_framework import generics
from m_s_server.services import message as message_service
from m_s_server.serializers import message as message_serializer
from rest_framework import permissions
from m_s_server.utils.serializer_mixins import CreateModelWithFullResultMixin


class MessageListCreateApi(CreateModelWithFullResultMixin, generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    write_serializer_class = message_serializer.MessageSerializer
    read_serializer_class = message_serializer.MessageFullSerializer
    queryset = message_service.get_all_messages()


class MessageRetrieveDestroyApi(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = message_serializer.MessageFullSerializer
    queryset = message_service.get_all_messages()


class MessageUserListApi(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = message_serializer.MessageFullSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = message_service.get_user_messages(user_id)
        return queryset


message_list_create_api = MessageListCreateApi.as_view()
message_retrieve_destroy_api = MessageRetrieveDestroyApi.as_view()
message_user_list_api = MessageUserListApi.as_view()
