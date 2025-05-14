from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):  # Исправлено: добавлено models.Model
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        help_text='Например: "Супы", "Десерты", "Напитки"'
    )
    order = models.PositiveIntegerField(  # Добавлено поле для сортировки
        default=0,
        verbose_name='Порядок сортировки'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='dishes',
        verbose_name='Категория',
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название блюда'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        help_text='Заполните описание'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Цена'
    )

    volume = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Объем/вес',
        help_text='Например: "0.5л", "150гр"'
    )

    image = models.ImageField(
        upload_to='dishes/',
        blank=True,
        null=True,
        verbose_name='Изображение блюда'
    )

    created_at = models.DateTimeField(  # Добавлено поле даты создания
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['category__order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"
