from django.urls import path
from . import views
from menu.apps import MenuConfig
from menu.views import (DishListView, CategoryListView, CategoryDetailView, DishDetailView, DishCreateView,
                        CategoryCreateView, DishUpdateView, CategoryUpdateView, DishDeleteView, CategoryDeleteView)

app_name = MenuConfig.name

urlpatterns = [
    path('dishes/', DishListView.as_view(), name='menu_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('menu/<int:pk>/', CategoryDetailView.as_view(), name='category_dishes'),
    path('dish_detail/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('menu/dish_create/', DishCreateView.as_view(), name='dish_create'),
    path('menu/category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('dish/<int:pk>/update/', DishUpdateView.as_view(), name='dish_update'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('dish/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete')
]
