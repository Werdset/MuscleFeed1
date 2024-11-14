from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('privacy-policy/', TemplateView.as_view(template_name="core/privacy_policy.html"), name='privacy_policy'),
    path('terms/', TemplateView.as_view(template_name="core/terms.html"), name='terms'),
]
