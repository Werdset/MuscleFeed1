from django.urls import path
from . import views

urlpatterns = [
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/callbacks/<int:callback_id>/update_status/', views.update_callback_status, name='update_callback_status'),
]
