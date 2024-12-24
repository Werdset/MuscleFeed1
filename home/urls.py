from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal-cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('personal-cabinet/profile/', views.profile_settings, name='profile_settings'),
    path('personal-cabinet/security/', views.account_security, name='account_security'),
    path('personal-cabinet/orders/', views.account_orders, name='account_orders'),
    path('order/configuration/<int:order_id>/', views.order_configuration, name='order_configuration'),
    path('order/summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('contacts/', views.contacts, name='contacts'),
    path('rations/balanced/', views.ration_balanced, name='ration_balanced'),
    path('rations/detox/', views.ration_detox, name='ration_detox'),
    path('rations/mass/', views.ration_mass, name='ration_mass'),
    path('rations/dry/', views.ration_dry, name='ration_dry'),
    path('delivery/', views.delivery, name='delivery'),
    path('certificates/', views.certificates, name='certificates'),
    path('discounts/', views.discounts, name='discounts'),
    path('menu_tariffs/', views.menu_tariffs, name='menu_tariffs'),
    path('partner_cabinet/', views.partner_cabinet, name='partner_cabinet'),
    path('public_offer/', views.public_offer, name='public_offer'),
    path('payment_methods/', views.payment_methods, name='payment_methods'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('site_map/', views.site_map, name='site_map'),
]
