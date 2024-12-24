from datetime import timedelta

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Order, OrderFreeze, CallbackRequest
from .forms import OrderForm, OrderFreezeForm
from .utils import calculate_order_price


@login_required
def make_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.user = request.user
        order.save()
        return redirect('orders:order_list')
    return render(request, 'orders/make_order.html', {'form': form})

@login_required
def account_order_freeze(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    form = OrderFreezeForm(request.POST or None)
    if form.is_valid():
        freeze = form.save(commit=False)
        freeze.order = order
        freeze.save()
        return redirect('orders:order_detail', order_id=order.id)
    return render(request, 'orders/order_freeze.html', {'form': form, 'order': order})

@login_required
def account_order_unfreeze(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.freezes.filter(active=True).update(active=False)
    return redirect('orders:order_detail', order_id=order.id)

@login_required
def account_order_extend(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status != 'completed':
        additional_days = 7
        if order.end_date:
            order.end_date += timedelta(days=additional_days)
        else:
            order.end_date = timezone.now() + timedelta(days=additional_days)
        order.total_price = calculate_order_price(order)
        order.save()

    return redirect('orders:order_detail', order_id=order.id)

def test_order(request):
    """Обработка пробного заказа"""
    if request.method == "POST":
        # Здесь можно добавить логику для создания пробного заказа
        order = Order.objects.create(user=request.user, total_price=500.00, status="active")
        return JsonResponse({"status": "success", "message": "Пробный заказ оформлен"})
    return JsonResponse({"status": "error", "message": "Не удалось оформить пробный заказ"})


def request_callback(request):
    """Обработка заявки на обратный звонок"""
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")

        # Проверка, что поля не пустые
        if not name or not phone:
            return JsonResponse({"status": "error", "message": "Пожалуйста, заполните все поля."})

        # Создание заявки на обратный звонок в базе данных
        callback = CallbackRequest.objects.create(name=name, phone=phone)

        # Здесь можно добавить логику для отправки уведомлений (например, по email) о новой заявке
        # Например, отправка email-уведомления
        # send_mail("Новая заявка на обратный звонок", f"Заявка от {name} с телефоном {phone}", "info@example.com", ["admin@example.com"])

        return JsonResponse({"status": "success", "message": "Спасибо! Мы скоро с вами свяжемся."})

    return JsonResponse({"status": "error", "message": "Произошла ошибка"})