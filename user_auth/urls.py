from django.urls import path
from .views import SignupAPI, LoginAPI, ResetPasswordAPI

urlpatterns = [
    path('signup/', SignupAPI.as_view(), name='signup'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('reset-password/<int:user_id>/', ResetPasswordAPI.as_view(), name='reset-password'),
]