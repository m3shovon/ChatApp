from core import consumers

# from django.conf.urls import url
from django.urls import re_path


websocket_urlpatterns = [
    # url(r'^ws$', consumers.ChatConsumer),
    re_path(r'^ws$', consumers.ChatConsumer.as_asgi()),
]
