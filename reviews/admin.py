from django.contrib import admin
from .models import Review, QuestionBlock, Question

# Настройка админки для отзывов
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at', 'is_published')
    list_filter = ('rating', 'is_published', 'created_at')
    search_fields = ('user__username', 'content')
    ordering = ('-created_at',)  # Сортировка по дате создания в порядке убывания

    def get_rating(self, obj):
        return f"{obj.rating} звезд"
    get_rating.short_description = 'Рейтинг'

# Настройка админки для блоков вопросов
class QuestionBlockAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Настройка админки для вопросов
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('block', 'question', 'answer')
    list_filter = ('block',)
    search_fields = ('question', 'answer')

# Регистрация моделей в админке
admin.site.register(Review, ReviewAdmin)
admin.site.register(QuestionBlock, QuestionBlockAdmin)
admin.site.register(Question, QuestionAdmin)