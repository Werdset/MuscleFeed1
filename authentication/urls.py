from django.urls import path
from .views import signup, login_view, logout_view, account_change_email, account_change_personal_data

urlpatterns = [
    path('signup/step-<int:step>/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-email/', account_change_email, name='change_email'),
    path('change-personal-data/', account_change_personal_data, name='change_personal_data'),
]
