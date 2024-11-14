from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/<int:menu_id>/', views.menu_detail, name='menu_detail'),
    path('menu-types/', views.menu_type_list, name='menu_type_list'),
    path('menu-types/<int:menu_type_id>/', views.menu_type_detail, name='menu_type_detail'),
]
