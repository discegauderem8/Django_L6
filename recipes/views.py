from django.shortcuts import render, redirect
from .models import Recipe, Category, Storage
from .forms import RecipeForm, CategoryForm, StorageForm, SearchForm


def index(request):
    return render(request, "recipes/index.html")

def show_items(request, model_name):
    if model_name == 'recipe':
        items = Recipe.objects.all()
    elif model_name == 'category':
        items = Category.objects.all()
    elif model_name == 'storage':
        items = Storage.objects.all()
    else:
        items = []
    return render(request, 'recipes/show_items.html', {'items': items, 'model_name': model_name})

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_items', model_name='recipe')  # Перенаправление на show_items с указанием модели
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_items', model_name='category')  # Указываем модель "category" для отображения объектов
    else:
        form = CategoryForm()
    return render(request, 'recipes/create_category.html', {'form': form})

def create_storage(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_items', model_name='storage')  # Указываем модель "storage" для отображения объектов
    else:
        form = StorageForm()
    return render(request, 'recipes/create_storage.html', {'form': form})
def name_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            search_recipes = form.cleaned_data.get('recipe_check')
            search_categories = form.cleaned_data.get('category_check')
            search_storages = form.cleaned_data.get('storage_check')
            recipes = Recipe.objects.filter(name=name) if search_recipes else []
            categories = Category.objects.filter(name=name) if search_categories else []
            storages = Storage.objects.filter(name=name) if search_storages else []
            return render(request, 'name_search_results.html', {'recipes': recipes, 'categories': categories, 'storages': storages})
    else:
        form = SearchForm()
    return render(request, 'recipes/name_search.html', {'form': form})

def name_search_results(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            search_recipes = form.cleaned_data.get('recipe_check')
            search_categories = form.cleaned_data.get('category_check')
            search_storages = form.cleaned_data.get('storage_check')
            recipes = Recipe.objects.filter(name=name) if search_recipes else []
            categories = Category.objects.filter(name=name) if search_categories else []
            storages = Storage.objects.filter(name=name) if search_storages else []
            return render(request, 'recipes/name_search_results.html', {'recipes': recipes, 'categories': categories, 'storages': storages})
    else:
        form = SearchForm()
    return redirect('name_search')  # Если запрос не POST, перенаправляем обратно на страницу поиска


