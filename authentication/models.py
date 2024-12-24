from django.db import models
from django.contrib.auth.models import User
import random


class Profile(models.Model):
    STATUS_CHOICES = [('activation', 'Отправлена ссылка активации'), ('active', 'Активен'), ('ban', 'Забанен')]
    LANGUAGE_CHOICES = [('ru', 'Русский'), ('he', 'Иврит')]
    SEX_CHOICES = [('male', 'Мужской'), ('female', 'Женский')]

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=150, null=True, blank=True)
    surname = models.CharField('Фамилия', max_length=150, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=150, null=True, blank=True)
    main_address = models.CharField('Основной адрес', max_length=255, null=True, blank=True)
    other_addresses = models.TextField('Другие адреса', null=True, blank=True)  # Храним как текст, каждый адрес с новой строки
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def get_other_addresses(self):
        if self.other_addresses:
            return self.other_addresses.split("\n")
        return []

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

