from django.shortcuts import render, redirect
from django.http import HttpResponse

from dishes.models import Dish
from orders.models import Order
from .models import Report
import xlsxwriter
from io import BytesIO

from django.shortcuts import render
from .models import Report

def generate_report(request, report_type):
    """Функция для генерации отчета в зависимости от его типа"""
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    if report_type == 'orders':
        worksheet.write('A1', 'ID Заказа')
        worksheet.write('B1', 'Дата')
        worksheet.write('C1', 'Сумма')

        # Добавляем данные из базы
        orders = Order.objects.filter(user=request.user)
        row = 1
        for order in orders:
            worksheet.write(row, 0, order.id)
            worksheet.write(row, 1, order.created_at.strftime('%Y-%m-%d'))
            worksheet.write(row, 2, str(order.total_price))
            row += 1
    elif report_type == 'dishes':
        worksheet.write('A1', 'ID Блюда')
        worksheet.write('B1', 'Название')
        worksheet.write('C1', 'Цена')

    # Добавляем данные из базы
        dishes = Dish.objects.all()
        row = 1
        for dish in dishes:
            worksheet.write(row, 0, dish.id)
            worksheet.write(row, 1, dish.name)
            worksheet.write(row, 2, str(dish.price))
            row += 1
        # Здесь добавляем данные из базы данных

    workbook.close()
    output.seek(0)

    # Сохраняем отчет в модель Report
    report = Report.objects.create(
        user=request.user,
        report_type=report_type,
    )
    report.file_path.save(f"{report_type}_report_{report.id}.xlsx", output)
    return redirect('reports:report_list')

def download_report(request, report_id):
    """Функция для скачивания сгенерированного отчета"""
    report = Report.objects.get(id=report_id, user=request.user)
    response = HttpResponse(report.file_path, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{report.file_path.name}"'
    return response




def report_list(request):
    """Функция для отображения списка отчетов пользователя"""
    reports = Report.objects.filter(user=request.user)
    return render(request, 'reports/report_list.html', {'reports': reports})
