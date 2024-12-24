from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.utils.translation import gettext_lazy as _
from orders.models import Order, CallbackRequest


@login_required
def manager_dashboard(request):
    """Страница для менеджеров с заказами и заявками на обратный звонок"""
    if not request.user.is_staff:
        return redirect('home')  # или возвращаем ошибку 403

    # Получаем все заказы и все заявки на обратный звонок
    orders = Order.objects.all()
    callbacks = CallbackRequest.objects.all()

    return render(request, 'dashboard/manager_dashboard.html', {
        'orders': orders,
        'callbacks': callbacks,
    })


def generate_order_pdf(request, order_id):
    """Функция для генерации PDF с данными на русском и иврите"""
    order = Order.objects.get(id=order_id)

    # Создаем пустой PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # Устанавливаем шрифт для иврита (здесь используется шрифт с поддержкой иврита, например, Arial)
    c.setFont("Helvetica", 12)

    # Заголовок на русском
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, _("Отчет по заказу"))

    # Информация о заказе на русском
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, _("Заказ ID:") + f" {order.id}")
    c.drawString(100, 680, _("Дата создания:") + f" {order.created_at}")
    c.drawString(100, 660, _("Общая сумма:") + f" {order.total_price} ₽")
    c.drawString(100, 640, _("Статус:") + f" {order.get_status_display()}")

    # Разделение между языками
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 600, _("גרסה עברית"))  # Заголовок на иврите

    # Информация о заказе на иврите
    c.setFont("Helvetica", 12)
    # Для иврита нужно учитывать направление текста (справа налево)
    c.drawRightString(500, 580, _("מספר הזמנה:") + f" {order.id}")
    c.drawRightString(500, 560, _("תאריך יצירה:") + f" {order.created_at}")
    c.drawRightString(500, 540, _("סך הכל:") + f" {order.total_price} ₪")  # Сумма на иврите (евро)
    c.drawRightString(500, 520, _("סטטוס:") + f" {order.get_status_display()}")

    # Сохраняем PDF в буфер
    c.showPage()
    c.save()

    # Подготовка ответа с PDF
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order.id}_report_bilingual.pdf"'

    return response