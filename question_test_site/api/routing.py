from django.urls import path
from api.consumers import WSConsumer, CommentConsumer

ws_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi()),
    path('ws/testrun/<int:pk>/comments/', CommentConsumer.as_asgi())
]
