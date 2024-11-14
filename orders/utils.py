from .models import Order, OrderFreeze
from datetime import timedelta
from django.utils import timezone


def calculate_order_price(order):
    """Вычисляет общую стоимость заказа на основе активных дней"""
    daily_rate = 10  # Предположим, что стоимость дня составляет 10 единиц валюты
    active_days = 0

    # Вычисляем количество дней между началом и концом заказа
    if order.start_date and order.end_date:
        current_date = order.start_date
        while current_date <= order.end_date:
            # Проверяем, попадает ли текущий день под заморозку
            if not order.freezes.filter(frozen_from__lte=current_date, frozen_to__gte=current_date).exists():
                active_days += 1
            current_date += timedelta(days=1)

    # Рассчитываем общую стоимость
    total_price = active_days * daily_rate
    return total_price
