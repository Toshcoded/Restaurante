from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from catalog.forms import PizzaForm
from catalog.models import Ingredient, Pizza


def index(request):
    return render(request, 'catalog/home.html')


class IngredientsListView(ListView):
    model = Ingredient
    paginate_by = 20  # if pagination is desired
    template_name = 'catalog/ingredients/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'List'
        return context


class IngredientsCreateView(CreateView):
    model = Ingredient
    fields = '__all__'
    template_name = 'catalog/ingredients/create.html'
    success_url = reverse_lazy('catalog_ingredients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'Create'
        return context


class IngredientsUpdate(UpdateView):
    model = Ingredient
    fields = '__all__'
    template_name = 'catalog/ingredients/update.html'
    success_url = reverse_lazy('catalog_ingredients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'Update'
        return context


class IngredientsDelete(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('catalog_ingredients')
    template_name = 'catalog/ingredients/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'Delete'
        return context


class PizzasListView(ListView):
    model = Pizza
    paginate_by = 20  # if pagination is desired
    template_name = 'catalog/pizzas/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'List'
        return context



class PizzasCreateView(CreateView):
    model = Pizza
    template_name = 'catalog/pizzas/create.html'
    success_url = reverse_lazy('catalog_pizzas')
    form_class = PizzaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'Create'
        return context


def pizza_create(request):
    if request.method == 'POST':
        form = PizzaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog_pizzas')
        else:
            return render(request, 'catalog/pizzas/create.html', {'form': form})
    else:
        form = PizzaForm()
        return render(request, 'catalog/pizzas/create.html', {'form': form})


class PizzasUpdate(UpdateView):
    model = Pizza
    fields = '__all__'
    template_name = 'catalog/pizzas/update.html'
    success_url = reverse_lazy('catalog_pizzas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'Update'
        return context


class PizzasDelete(DeleteView):
    model = Pizza
    success_url = reverse_lazy('catalog_pizzas')
    template_name = 'catalog/pizzas/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = 'Delete'
        return context
