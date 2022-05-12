"""Defining URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Page for a single pizza.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]