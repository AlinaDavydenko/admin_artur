from django.urls import path
from . import views
from pub_menu.apps import PubMenuConfig
from pub_menu.views import index

app_name = PubMenuConfig.name

urlpatterns = [
    path('', views.index, name='index')
]
