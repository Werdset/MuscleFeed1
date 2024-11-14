from django.urls import path
from .views import make_order, account_order_freeze, account_order_unfreeze, account_order_extend

app_name = 'orders'

urlpatterns = [
    path('make-order/', make_order, name='make_order'),
    path('order/<int:order_id>/freeze/', account_order_freeze, name='order_freeze'),
    path('order/<int:order_id>/unfreeze/', account_order_unfreeze, name='order_unfreeze'),
    path('order/<int:order_id>/extend/', account_order_extend, name='order_extend'),
]
