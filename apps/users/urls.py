from django.urls import path
from .views import Login, Register

urlpatterns = [
    path('auth/login/', Login.as_view(), name='login'),
    path('auth/register/', Register.as_view(), name='register')
]
