from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from catalog.models import Ingredient, Pizza
from .serializers import PizzaSerializer
from rest_framework import generics


class ResponseJSON(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(ResponseJSON, self).__init__(content, **kwargs)


@api_view(['GET'])
def get_pizzas(request):
    return ResponseJSON(PizzaSerializer(Pizza.objects.all(), many=True).data)
