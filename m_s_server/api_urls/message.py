from django.conf.urls import url
from m_s_server.views import message

message_urlpatterns = [
    url(r'^messages/$', message.message_list_create_api, name='m_list_create_api'),
    url(r'^messages/(?P<pk>\d+)/$', message.message_destroy_api, name='m_destroy_api'),
    url(r'^messages/user/$', message.message_user_list_api, name='m_user_list_api_api')
]
