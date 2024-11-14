# Generated by Django 5.1.3 on 2024-11-14 14:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_email', models.EmailField(max_length=120, verbose_name='Новый e-mail')),
                ('key', models.CharField(max_length=6, verbose_name='Ключ подтверждения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия')),
                ('sex', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', max_length=6, verbose_name='Пол')),
                ('status', models.CharField(choices=[('activation', 'Отправленна ссылка активации'), ('active', 'Активен'), ('ban', 'Забанен')], default='activation', max_length=10, verbose_name='Статус')),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('he', 'Иврит')], default='ru', max_length=2, verbose_name='Язык')),
                ('phone', models.CharField(blank=True, max_length=150, null=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Адрес')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='Модератор')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='ChangePersonalDataRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.CharField(max_length=20, verbose_name='Новые данные')),
                ('type', models.CharField(choices=[('name', 'Имя'), ('surname', 'Фамилия'), ('phone', 'Телефон'), ('address', 'Адрес')], default='name', max_length=13, verbose_name='Тип')),
                ('done', models.BooleanField(default=False, verbose_name='Выполнить')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='Профиль')),
            ],
        ),
        migrations.CreateModel(
            name='ResetPasswordVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=6, verbose_name='Ключ подтверждения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
