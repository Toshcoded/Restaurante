from django.urls import path

from catalog.models import Ingredient, Pizza
from catalog.rest import get_pizzas
from catalog.views import index, IngredientsCreateView, IngredientsDelete, IngredientsUpdate, \
    IngredientsListView, PizzasListView, PizzasUpdate, PizzasDelete, pizza_create, PizzasCreateView

urlpatterns = [
    path('', index, name='catalog_home'),
    path('ingredients/', IngredientsListView.as_view(), name='catalog_ingredients'),
    path('ingredients/create/', IngredientsCreateView.as_view(), name='catalog_ingredients_create'),
    path('ingredients/update/<int:pk>/', IngredientsUpdate.as_view(), name='catalog_ingredients_update'),
    path('ingredients/delete/<int:pk>/', IngredientsDelete.as_view(), name='catalog_ingredients_delete'),

    path('pizzas/', PizzasListView.as_view(), name='catalog_pizzas'),
    # path('pizzas/create/', pizza_create, name='catalog_pizzas_create'),
    path('pizzas/create/', PizzasCreateView.as_view(), name='catalog_pizzas_create'),
    # path('pizzas/update/<int:pk>/', pizza_update, name='catalog_pizzas_update'),
    path('pizzas/update/<int:pk>/', PizzasUpdate.as_view(), name='catalog_pizzas_update'),
    path('pizzas/delete/<int:pk>/', PizzasDelete.as_view(), name='catalog_pizzas_delete'),

    path('api/pizzas/', get_pizzas)
]
