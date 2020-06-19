from django.conf.urls import url
from m_s_server.views import user

user_urlpatterns = [
    url(r'^users/$', user.user_list_api, name='u_list_api'),
    url(r'^users/me/$', user.user_me_api, name='user_me_pi'),
]
