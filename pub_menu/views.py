from django.shortcuts import render

from menu.models import Category, Dish


# Create your views here.
def index(request):
    categories = Category.objects.prefetch_related('dishes').order_by('order')

    menu_data = {}
    for category in categories:
        menu_data[category.name] = [
            {
                "item_id": str(dish.id),
                "name": dish.name,
                "desc": dish.description,
                "price": float(dish.price),  # Преобразуем Decimal в float для JSON
                "volume": ""  # Добавляем пустое поле volume, если оно у вас есть в модели
            }
            for dish in category.dishes.all().order_by('name')
        ]

    context = {
        'menu_data': menu_data
    }
    return render(request, 'pub_menu/index.html', context)
