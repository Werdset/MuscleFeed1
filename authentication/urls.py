from django.urls import path

from . import views
from .views import signup, login_view, logout_view, account_change_email, account_change_personal_data, \
    reset_password_request, reset_password_verify

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', reset_password_request, name='reset_password_request'),
    path('password_reset/verify/', reset_password_verify, name='reset_password_verify'),
    path('logout/', logout_view, name='logout'),
    path('change-email/', account_change_email, name='change_email'),
    path('change-personal-data/', account_change_personal_data, name='change_personal_data'),
]
