from django import forms
from .models import Recipe, Category, Storage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # fields = ['name', 'description', 'guide', 'timing', 'author', 'image']
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = ['name', 'description']
        fields = '__all__'

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        # fields = ['name', 'items', 'categories']
        fields = '__all__'


class SearchForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField(label='Name', max_length=200,required=False)
    description = forms.CharField(label='Description', max_length=1000, required=False)
    recipe_check = forms.BooleanField(label='Search in Recipes', required=False)
    category_check = forms.BooleanField(label='Search in Categories', required=False)
    storage_check = forms.BooleanField(label='Search in Storages', required=False)