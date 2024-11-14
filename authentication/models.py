from django.db import models
from django.contrib.auth.models import User
import random


class Profile(models.Model):
    STATUS_CHOICES = [('activation', 'Отправленна ссылка активации'), ('active', 'Активен'), ('ban', 'Забанен')]
    LANGUAGE_CHOICES = [('ru', 'Русский'), ('he', 'Иврит')]
    SEX_CHOICES = [('male', 'Мужской'), ('female', 'Женский')]

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=150, null=True, blank=True)
    surname = models.CharField('Фамилия', max_length=150, null=True, blank=True)
    sex = models.CharField('Пол', max_length=6, choices=SEX_CHOICES, default='male')
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='activation')
    language = models.CharField('Язык', max_length=2, choices=LANGUAGE_CHOICES, default='ru')
    phone = models.CharField('Телефон', max_length=150, null=True, blank=True)
    address = models.CharField('Адрес', max_length=150, null=True, blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    is_moderator = models.BooleanField('Модератор', default=False)

    def __str__(self):
        return self.user.username


class EmailVerification(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    new_email = models.EmailField('Новый e-mail', max_length=120)
    key = models.CharField('Ключ подтверждения', max_length=6)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs):
        self.key = '{:06}'.format(random.randint(1, 1000000))
        super().save(*args, **kwargs)


class ResetPasswordVerification(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    key = models.CharField('Ключ подтверждения', max_length=6)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs):
        self.key = '{:06}'.format(random.randint(1, 1000000))
        super().save(*args, **kwargs)


class ChangePersonalDataRequest(models.Model):
    TYPE_CHOICES = [('name', 'Имя'), ('surname', 'Фамилия'), ('phone', 'Телефон'), ('address', 'Адрес')]
    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.CASCADE)
    new = models.CharField('Новые данные', max_length=20)
    type = models.CharField('Тип', max_length=13, choices=TYPE_CHOICES, default='name')
    done = models.BooleanField('Выполнить', default=False)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.done:
            setattr(self.profile, self.type, self.new)
            self.profile.save()
            self.delete()
        else:
            super().save(*args, **kwargs)

