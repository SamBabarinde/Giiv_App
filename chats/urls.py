from django.urls import path

from . import views


app_name = "chats"

urlpatterns = [
    path('new/<int:ipk>/', views.New_conversation, name="new"),
    path('inbox/', views.inbox, name="inbox"),
    path('messages/<int:pk>/', views.directMessage, name="dm"),
]
