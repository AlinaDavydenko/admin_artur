# Generated by Django 4.2.2 on 2025-05-14 10:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: "Супы", "Десерты", "Напитки"', max_length=100, verbose_name='Название категории')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('description', models.TextField(blank=True, help_text='Заполните описание', verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('volume', models.CharField(blank=True, help_text='Например: "0.5л", "150гр"', max_length=50, verbose_name='Объем/вес')),
                ('image', models.ImageField(blank=True, null=True, upload_to='dishes/', verbose_name='Изображение блюда')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menu.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ['category__order', 'name'],
            },
        ),
    ]
