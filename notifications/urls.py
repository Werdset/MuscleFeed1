from django.shortcuts import render
from django.urls import path
from .views import process_call_request

app_name = 'notifications'

urlpatterns = [
    path('call-request/', process_call_request, name='call_request'),
    path('call-request/success/', lambda request: render(request, 'notifications/success.html'), name='call_request_success'),
]
