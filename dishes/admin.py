from django.contrib import admin
from .models import Dish, MenuType, Menu
from django.utils.html import format_html

# Админка для модели Dish
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'calories', 'weight', 'proteins', 'fats', 'carbohydrates', 'image_tag')
    search_fields = ('name', 'type', 'description')
    list_filter = ('type',)
    ordering = ('name',)
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'image', 'description', 'calories', 'weight', 'proteins', 'fats', 'carbohydrates')
        }),
        ('Изображение', {
            'fields': ('image_tag',)
        }),
    )

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url) if obj.image else ''
    image_tag.short_description = 'Изображение'

# Админка для модели MenuType
class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'extra_short_description', 'image_tag')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'fields': ('name', 'short_description', 'extra_short_description', 'description', 'image')
        }),
        ('Изображение', {
            'fields': ('image_tag',)
        }),
    )

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url) if obj.image else ''
    image_tag.short_description = 'Изображение'

# Админка для модели Menu
class MenuAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'calories', 'price', 'image_tag')
    search_fields = ('name', 'description', 'type__name')
    list_filter = ('type', 'calories', 'price')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('type', 'name', 'description', 'calories', 'days', 'price')
        }),
    )

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.type.image.url) if obj.type.image else ''
    image_tag.short_description = 'Изображение'

# Регистрация моделей в админке
admin.site.register(Dish, DishAdmin)
admin.site.register(MenuType, MenuTypeAdmin)
admin.site.register(Menu, MenuAdmin)