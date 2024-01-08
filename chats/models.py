from django.db import models
from core.models import Item
from userauth.models import User

class Conversations(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-modified_at',)
        
        
class ChatMessage(models.Model):
    conversation = models.ForeignKey(Conversations, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='created_massages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    