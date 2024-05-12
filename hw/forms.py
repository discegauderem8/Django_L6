from django import forms
from django.forms import RadioSelect, Select, CheckboxInput, NumberInput, SelectMultiple

from .models import Customer, Item, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'items', 'total_amount']
        widgets = {"customer": RadioSelect, "total_amount": NumberInput}

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'count']

class ImageForm(forms.Form):
    image = forms.ImageField()

