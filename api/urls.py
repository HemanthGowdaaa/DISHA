from django.urls import path
from .views import register_user, login_user, help_request

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('help/', help_request, name='help_request'),
]
