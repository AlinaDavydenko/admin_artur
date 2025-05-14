from django.contrib import admin
from menu.models import Dish, Category


# Register your models here.
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price')
    list_filter = ('category',)
    search_fields = ('name',)

    list_editable = ('price',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_filter = ('order',)
    search_fields = ('name',)
