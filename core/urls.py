from django.urls import path
from core import views


app_name = 'core'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.details, name='details'),
    path('post-item/', views.postItem, name='post-item'),
    path('search/', views.searchItem, name='search'),
]
