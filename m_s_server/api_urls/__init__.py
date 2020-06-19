from m_s_server.api_urls.auth import auth_urlpatterns
from m_s_server.api_urls.message import message_urlpatterns
from m_s_server.api_urls.user import user_urlpatterns

api_urlpatterns = []

api_urlpatterns += auth_urlpatterns
api_urlpatterns += message_urlpatterns
api_urlpatterns += user_urlpatterns
