from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Category, Dish
from django.urls import reverse_lazy
from django.db.models import query


class DishListView(ListView):
    model = Dish
    # menu/dish_list.html


class DishDetailView(DetailView):
    model = Dish
# dish_detail.html


class CategoryListView(ListView):
    model = Category
    # category_list.html


class CategoryDetailView(DetailView):
    model = Category


class DishCreateView(CreateView):
    model = Dish
    fields = ('name', 'category', 'description', 'price')
    success_url = reverse_lazy('menu:menu_list')


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name', 'order')
    success_url = reverse_lazy('menu:category_list')


class DishUpdateView(UpdateView):
    model = Dish
    fields = ('name', 'category', 'description', 'price')
    success_url = reverse_lazy('menu:menu_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name', 'order')
    success_url = reverse_lazy('menu:category_list')


class DishDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy('menu:menu_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('menu:category_list')
