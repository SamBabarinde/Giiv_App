from django.contrib import admin
from django.urls import path, include


# will not be in production
from django.conf import settings
from django.conf.urls.static import static

# google login
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('', include("base.urls")),
    path('', include("userauth.urls")),
    path('', include("chats.urls")),
    
    path('', include('oauth_app.urls')),
    
    #... google login
    # path('', TemplateView.as_view(template_name="core/login.html")),
    # path('', include('googleauthentication.urls')),
    path('accounts/', include('allauth.urls')),
    # path('logout', LogoutView.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)