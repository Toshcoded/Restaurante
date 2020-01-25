from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Pizza
        fields = '__all__'
