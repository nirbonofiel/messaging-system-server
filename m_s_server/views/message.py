from rest_framework import generics
from m_s_server.services import message as message_service
from m_s_server.serializers import message as message_serializer
from rest_framework import authentication, permissions


class MessageListCreateApi(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = message_serializer.MessageSerializer
    queryset = message_service.get_all_messages()


class MessageDestroyApi(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = message_service.get_all_messages()


class MessageListByReceiverApi(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = message_serializer.MessageSerializer

    def get_queryset(self):
        queryset = message_service.get_messages_by_receiver(self.request.data['receiver'])
        return queryset


message_list_create_api = MessageListCreateApi.as_view()
message_destroy_api = MessageDestroyApi.as_view()
message_list_by_receiver_api = MessageListByReceiverApi.as_view()
