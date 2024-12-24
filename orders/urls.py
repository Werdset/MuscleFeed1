from django.urls import path

from . import views
from .views import make_order, account_order_freeze, account_order_unfreeze, account_order_extend

app_name = 'orders'

urlpatterns = [
    path('make-order/', make_order, name='make_order'),
    path('order/<int:order_id>/freeze/', account_order_freeze, name='order_freeze'),
    path('order/<int:order_id>/unfreeze/', account_order_unfreeze, name='order_unfreeze'),
    path('order/<int:order_id>/extend/', account_order_extend, name='order_extend'),
    path('orders/test/', views.test_order, name='test_order'),
    path('orders/request_callback/', views.request_callback, name='request_callback'),
]
