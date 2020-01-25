from rest_framework import serializers

from catalog.models import Ingredient, Pizza


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    # price = serializers.SerializerMethodField(source='get_price()')

    class Meta:
        model = Pizza
        fields = ('name', 'price', 'ingredients', 'image')
