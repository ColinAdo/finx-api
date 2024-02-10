from django.urls import path

from .views import ChatListCreateView, ChatDetailView, MessageDetailView

urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chats'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),

    path('chats/<int:pk>/message/<int:message_pk>/',
         MessageDetailView.as_view(), name='message-detail'),
]