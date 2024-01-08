from django.urls import path
from userauth import views
from django.contrib.auth import views as authview

from .forms import LoginForm

app_name = 'userauth'

urlpatterns = [
    path('register/', views.signUp, name='signup'),
    # path('login/', views.signIn, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('login/', authview.LoginView.as_view(template_name="userauth/login.html", authentication_form=LoginForm), name='login'),
    path('activate/<uidb64>/<token>/', views.activateAccount, name='activate'),
    
    #  password changes
    path('change-password/', views.changePassword, name='change-password'),
    path('reset-password/', views.resetPassword, name='reset-password'),
    path('reset/<uidb64>/<token>/', views.confirmResetPassword, name='confirm-reset-password'),
    
]
