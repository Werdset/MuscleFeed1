from django.db import models

class Review(models.Model):
    """Модель для отзывов пользователей"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    content = models.TextField("Отзыв")
    rating = models.PositiveIntegerField("Рейтинг", default=5)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_published = models.BooleanField("Опубликован", default=False)

    def __str__(self):
        return f"Отзыв от {self.user.username} - {self.rating} звезд"

class QuestionBlock(models.Model):
    """Модель для блока вопросов"""
    title = models.CharField("Название блока", max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    """Модель для вопросов и ответов (FAQ)"""
    block = models.ForeignKey(QuestionBlock, related_name="questions", on_delete=models.CASCADE, verbose_name="Блок вопросов")
    question = models.CharField("Вопрос", max_length=255)
    answer = models.TextField("Ответ")

    def __str__(self):
        return f"Вопрос: {self.question}"
