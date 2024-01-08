from django.contrib import admin
from .models import ChatMessage, Conversations


admin.site.register(ChatMessage)
admin.site.register(Conversations)