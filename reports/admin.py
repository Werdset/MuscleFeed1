from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_report_type', 'generated_at', 'file_path')
    list_filter = ('report_type', 'generated_at')
    search_fields = ('user__username', 'report_type')
    ordering = ('-generated_at',)  # Сортировка по дате создания в порядке убывания

    def get_report_type(self, obj):
        return obj.get_report_type_display()
    get_report_type.short_description = 'Тип отчета'

# Регистрация модели в админке
admin.site.register(Report, ReportAdmin)