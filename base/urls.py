from django.urls import path
from base import views

app_name = 'base'


urlpatterns = [
    path('support/', views.support, name='support'),
    path('profile/', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.deleteItem, name='delete'),
    path('edit/<int:pk>/', views.editItem, name='edit'),
]
