from django.urls import path
from .views import reviews_show_all, write_review, faq

app_name = 'reviews'

urlpatterns = [
    path('', reviews_show_all, name='reviews_list'),
    path('write/', write_review, name='write_review'),
    path('faq/', faq, name='faq'),
]
