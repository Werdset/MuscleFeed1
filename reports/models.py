from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    """Модель для хранения данных о сгенерированных отчетах"""
    REPORT_TYPES = [
        ('orders', 'Отчет по заказам'),
        ('dishes', 'Отчет по блюдам'),
        ('delivery', 'Отчет по доставке'),
    ]

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    report_type = models.CharField("Тип отчета", max_length=20, choices=REPORT_TYPES)
    generated_at = models.DateTimeField("Дата создания", auto_now_add=True)
    file_path = models.FileField("Файл отчета", upload_to="reports/")

    def __str__(self):
        return f"{self.get_report_type_display()} от {self.generated_at.strftime('%Y-%m-%d')}"
