from django import forms
from .models import Recipe, Category, Storage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'guide', 'timing', 'author', 'image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['name', 'items', 'categories']


class SearchForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    recipe_check = forms.BooleanField(label='Search in Recipes', required=False)
    category_check = forms.BooleanField(label='Search in Categories', required=False)
    storage_check = forms.BooleanField(label='Search in Storages', required=False)