from django.contrib import admin
from .models import Order, OrderFreeze
from django.utils.html import format_html

# Админка для модели Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status', 'total_price', 'status_tag')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('status_tag',)

    def status_tag(self, obj):
        return format_html('<span style="color: {};">{}</span>',
                           'green' if obj.status == 'active' else 'red' if obj.status == 'frozen' else 'blue',
                           obj.get_status_display())
    status_tag.short_description = 'Статус'

# Админка для модели OrderFreeze
class OrderFreezeAdmin(admin.ModelAdmin):
    list_display = ('order', 'frozen_from', 'frozen_to', 'active')
    search_fields = ('order__id',)
    list_filter = ('active',)
    ordering = ('-frozen_from',)

# Регистрация моделей в админке
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderFreeze, OrderFreezeAdmin)