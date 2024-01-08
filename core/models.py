from django.db import models
from userauth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=False, default='the description of the item') 
    details = models.TextField(blank=True, null=True, default='more details about picking up, or the number to call') 
    location = models.CharField(max_length=150)
    state = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)  
    is_available = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Items'
    
    def __str__(self):
        return self.title
    
    