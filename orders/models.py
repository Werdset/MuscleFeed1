from django.db import models
from django.contrib.auth.models import User
import datetime

class Order(models.Model):
    STATUS_CHOICES = [('active', 'Активен'), ('frozen', 'Заморожен'), ('completed', 'Завершен')]

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='active')
    total_price = models.DecimalField('Общая цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Заказ {self.id} - {self.user.username} - {self.status}"

class OrderFreeze(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='freezes')
    frozen_from = models.DateField('Заморожено с', blank=True, null=True)
    frozen_to = models.DateField('Заморожено по', blank=True, null=True)
    active = models.BooleanField('Активно', default=True)

    def __str__(self):
        return f"Заморозка {self.order.id} с {self.frozen_from} по {self.frozen_to}"

def get_order_days(order):
    """Вспомогательная функция для расчета дней заказа"""
    # Логика расчета дней, когда заказ активен и не заморожен
    pass

class CallbackRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return f"Заявка от {self.name} ({self.phone})"
