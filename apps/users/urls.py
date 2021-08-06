from django.urls import path
from .views import Login, Register, UserInfo

urlpatterns = [
    path('auth/login/', Login.as_view(), name='login'),
    path('auth/register/', Register.as_view(), name='register'),
    path('user/', UserInfo.as_view(), name='user')
]
