from django.urls import path
from .views import generate_report, download_report

app_name = 'reports'

urlpatterns = [
    path('generate/<str:report_type>/', generate_report, name='generate_report'),
    path('download/<int:report_id>/', download_report, name='download_report'),
]
