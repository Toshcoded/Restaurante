from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        verbose_name = 'Sample'
        verbose_name_plural = 'Sample'

    def __str__(self):
        return '{} - {}'.format(self.name, self.price)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    @property
    def price(self):
        total_ingredients = 0
        ingredients = self.ingredients.select_related()
        for ingredient in ingredients:
            total_ingredients += ingredient.price
        return total_ingredients * 1.5
