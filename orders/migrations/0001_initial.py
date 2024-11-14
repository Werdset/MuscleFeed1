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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('active', 'Активен'), ('frozen', 'Заморожен'), ('completed', 'Завершен')], default='active', max_length=10, verbose_name='Статус')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общая цена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFreeze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frozen_from', models.DateField(blank=True, null=True, verbose_name='Заморожено с')),
                ('frozen_to', models.DateField(blank=True, null=True, verbose_name='Заморожено по')),
                ('active', models.BooleanField(default=True, verbose_name='Активно')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='freezes', to='orders.order', verbose_name='Заказ')),
            ],
        ),
    ]
