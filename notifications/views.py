from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import NotificationSettings, CallRequest
from .forms import CallRequestForm
import requests


def send_email_notification(subject, message, recipient_email):
    """Отправка email-уведомления"""
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        fail_silently=False,
    )


def send_whatsapp_message(phone_number, message):
    """Отправка WhatsApp-сообщения через API"""
    url = f"https://api.whatsapp.com/send?phone={phone_number}&text={message}"
    # Реальный API-запрос может потребовать использование POST-запроса
    response = requests.get(url)
    return response.ok


def process_call_request(request):
    """Обработка запроса на обратный звонок"""
    form = CallRequestForm(request.POST or None)
    if form.is_valid():
        call_request = form.save()
        message = f"Запрос на звонок от {call_request.name}, телефон: {call_request.phone}"

        # Отправка уведомления по email
        settings_obj = NotificationSettings.objects.first()
        if settings_obj and settings_obj.email_notifications:
            send_email_notification(
                "Новый запрос на обратный звонок",
                message,
                settings_obj.email_recipient
            )

        # Отправка уведомления по WhatsApp
        if settings_obj and settings_obj.whatsapp_notifications and settings_obj.whatsapp_number:
            send_whatsapp_message(settings_obj.whatsapp_number, message)

        return redirect('notifications:call_request_success')
    return render(request, 'notifications/call_request.html', {'form': form})
