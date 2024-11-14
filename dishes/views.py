from django.shortcuts import render, get_object_or_404
from .models import Dish, Menu, MenuType


# Список всех блюд
def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dishes/dish_list.html', {'dishes': dishes})

# Детали конкретного блюда
def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'dishes/dish_detail.html', {'dish': dish})

# Список всех меню
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'dishes/menu_list.html', {'menus': menus})

# Детали конкретного меню
def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    return render(request, 'dishes/menu_detail.html', {'menu': menu})

# Список всех типов меню
def menu_type_list(request):
    menu_types = MenuType.objects.all()
    return render(request, 'dishes/menu_type_list.html', {'menu_types': menu_types})

# Детали конкретного типа меню
def menu_type_detail(request, menu_type_id):
    menu_type = get_object_or_404(MenuType, id=menu_type_id)
    return render(request, 'dishes/menu_type_detail.html', {'menu_type': menu_type})
