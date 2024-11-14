from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Dish(models.Model):
    name = models.CharField('Название', max_length=120)
    type = models.CharField(
        'Тип',
        choices=[
            ('breakfast', 'Завтрак'),
            ('second-breakfast', 'Второй завтрак'),
            ('lunch', 'Обед'),
            ('high-tea', 'Полдник'),
            ('dinner', 'Ужин'),
            ('drink', 'Напиток')
        ],
        max_length=50
    )
    image = models.ImageField('Изображение', upload_to='dishes/')
    description = models.CharField('Описание', max_length=500)
    calories = models.IntegerField('Калории')
    weight = models.IntegerField('Вес в граммах')
    proteins = models.IntegerField('Белки')
    fats = models.IntegerField('Жиры')
    carbohydrates = models.IntegerField('Углеводы')

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Dish)
def add_webp_image(sender, instance, **kwargs):
    if instance.image:
        img = Image.open(instance.image.file)
        buffer = BytesIO()
        img.save(buffer, format='WEBP', quality=80)
        instance.image_webp.save(
            f"{instance.image.name.split('.')[0]}.webp",
            InMemoryUploadedFile(
                buffer, None, f"{instance.image.name.split('.')[0]}.webp", 'image/webp', img.size, None
            ),
            save=False
        )

class MenuType(models.Model):
    name = models.CharField('Полное название', max_length=50)
    short_description = models.CharField('Короткое описание', max_length=30)
    extra_short_description = models.CharField('Очень короткое описание', max_length=20, default='от 10$/мес')
    description = models.CharField('Описание', max_length=300)
    image = models.ImageField('Фоновое изображение', upload_to='menu-types/')

    def __str__(self):
        return self.name

class Menu(models.Model):
    type = models.ForeignKey(MenuType, on_delete=models.CASCADE, verbose_name='Тип меню')
    name = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=300)
    calories = models.IntegerField('Калорий', default=2000)
    days = models.JSONField('Блюда по дням', default=dict)
    price = models.DecimalField('Цена за день', max_digits=8, decimal_places=2, default=10.00)

    def __str__(self):
        return f"{self.type.name} - {self.name}"

