from django.conf.urls import url
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token , obtain_jwt_token
from m_s_server.views.auth import logout

auth_urlpatterns = [
    url(r'^login/$', obtain_jwt_token, name="login"),
    url(r'^token-refresh/$', refresh_jwt_token, name="token_refresh"),
    url(r'^token-verify/$', verify_jwt_token, name="token_verify"),
    url(r'^logout/$', logout, name="logout")
]
