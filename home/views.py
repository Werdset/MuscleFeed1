from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404

from authentication.models import Profile
from dishes.models import Dish, Menu
from orders.models import Order
from reviews.models import Review  # Предполагается, что модель отзывов находится в этом же приложении


def home(request):
    """Главная страница с данными из БД"""
    dishes = Dish.objects.all()[:6]  # Показываем 6 блюд
    menus = Menu.objects.all()[:3]  # Показываем 3 меню
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:3]  # Последние 3 отзыва

    context = {
        'dishes': dishes,
        'menus': menus,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)


@login_required
def personal_cabinet(request):
    """Главная страница личного кабинета"""
    return render(request, 'personal_cabinet.html')

@login_required
def profile_settings(request):
    """Страница профиля с контактными данными и адресами"""
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.surname = request.POST.get('surname')
        profile.phone = request.POST.get('phone')
        profile.main_address = request.POST.get('main_address')
        profile.other_addresses = request.POST.get('other_addresses')  # Сохраняем как текст
        profile.save()
        return redirect('profile_settings')

    context = {
        'profile': profile,
        'other_addresses': profile.get_other_addresses()
    }
    return render(request, 'profile_settings.html', context)

@login_required
def account_security(request):
    """Смена пароля"""
    form = PasswordChangeForm(user=request.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('personal_cabinet')
    return render(request, 'account_security.html', {'form': form})

def orders_view(request):
    """Отображение заказов с фильтрацией по статусу"""
    status = request.GET.get('status', 'all')  # Получаем параметр 'status' из URL
    if status == 'active':
        user_orders = Order.objects.filter(user=request.user, status='active')
    elif status == 'frozen':
        user_orders = Order.objects.filter(user=request.user, status='frozen')
    elif status == 'unpaid':
        user_orders = Order.objects.filter(user=request.user, status='unpaid')
    elif status == 'completed':
        user_orders = Order.objects.filter(user=request.user, status='completed')
    else:  # Все заказы
        user_orders = Order.objects.filter(user=request.user)

    context = {
        'orders': user_orders,
        'current_status': status,  # Передаём текущий статус для выделения активного пункта
    }
    return render(request, 'account_orders.html', context)

@login_required
def account_orders(request):
    """Просмотр заказов пользователя"""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'account_orders.html', {'orders': orders})

@login_required
def order_configuration(request, order_id):
    """Конфигурация рациона заказа"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        # Логика обработки изменения конфигурации
        # Например, обновление калорийности, блюд или дат
        order.calories = request.POST.get('calories', order.calories)
        order.duration = request.POST.get('duration', order.duration)
        order.allergens = request.POST.get('allergens', order.allergens)
        order.save()
        return redirect('account_orders')  # Возвращение на страницу заказов

    context = {
        'order': order,
    }
    return render(request, 'order_configuration.html', context)


@login_required
def order_summary(request, order_id):
    """Предварительный просмотр рациона заказа"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order,
    }
    return render(request, 'order_summary.html', context)

from django.shortcuts import render

def contacts(request):
    return render(request, 'contacts.html', {'title': 'Контакты'})

def ration_balanced(request):
    return render(request, 'ration_balanced.html', {'title': 'Сбалансированный рацион'})

def ration_detox(request):
    return render(request, 'ration_detox.html', {'title': 'Детокс'})

def ration_mass(request):
    return render(request, 'ration_mass.html', {'title': 'Рацион для набора массы'})

def ration_dry(request):
    return render(request, 'ration_dry.html', {'title': 'Рацион для сушки'})

def delivery(request):
    return render(request, 'delivery.html', {'title': 'Доставка'})

def certificates(request):
    return render(request, 'certificates.html', {'title': 'Сертификаты'})

def discounts(request):
    return render(request, 'discounts.html', {'title': 'Акции и скидки'})

def menu_tariffs(request):
    return render(request, 'menu_tariffs.html', {'title': 'Меню и тарифы'})

def partner_cabinet(request):
    return render(request, 'partner_cabinet.html', {'title': 'Кабинет партнера'})

def public_offer(request):
    return render(request, 'public_offer.html', {'title': 'Публичная оферта'})

def payment_methods(request):
    return render(request, 'payment_methods.html', {'title': 'Способы оплаты'})

def privacy_policy(request):
    return render(request, 'privacy_policy.html', {'title': 'Политика обработки персональных данных'})

def site_map(request):
    return render(request, 'site_map.html', {'title': 'Карта сайта'})