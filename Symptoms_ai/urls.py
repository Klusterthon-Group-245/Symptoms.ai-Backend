from django.urls import path
from .views import gpt3_api

urlpatterns = [
    path('gpt3-api/', gpt3_api, name='gpt3_api'),
]
