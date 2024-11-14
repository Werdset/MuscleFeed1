from django.db import models
from django.core.mail import send_mail

class NotificationSettings(models.Model):
    """Настройки уведомлений (email, WhatsApp, другие параметры)"""
    email_notifications = models.BooleanField('Включить email-уведомления', default=True)
    whatsapp_notifications = models.BooleanField('Включить WhatsApp-уведомления', default=True)
    email_recipient = models.EmailField('Email для уведомлений', max_length=254)
    whatsapp_number = models.CharField('Номер WhatsApp', max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Настройки уведомлений для {self.email_recipient}"

class CallRequest(models.Model):
    """Запрос на обратный звонок"""
    name = models.CharField('Имя и фамилия', max_length=150)
    phone = models.CharField('Телефон', max_length=150)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    processed = models.BooleanField('Обработан', default=False)

    def __str__(self):
        return f"Запрос на звонок от {self.name} - {self.phone}"
