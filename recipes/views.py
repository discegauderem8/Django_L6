from itertools import chain

from django.shortcuts import render, redirect

from .forms import RecipeForm, CategoryForm, StorageForm, SearchForm
from .models import Recipe, Category, Storage


def index(request):
    recipes = Recipe.objects.all().order_by('?')[:5]  # Получаем 5 случайных рецептов из базы данных
    return render(request, 'recipes/index.html', {'recipes': recipes})


def show_items(request, model_name="recipe"):
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
            id = form.cleaned_data.get('id')
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            search_recipes = form.cleaned_data.get('recipe_check')
            search_categories = form.cleaned_data.get('category_check')
            search_storages = form.cleaned_data.get('storage_check')

            recipes = Recipe.objects.all()
            categories = Category.objects.all()
            storages = Storage.objects.all()
            if id:
                final_recipes = recipes.filter(id=id)
                final_categories = categories.filter(id=id)
                final_storages = storages.filter(id=id)

                return render(request, 'recipes/name_search_results.html', {
                    'recipes': final_recipes,
                    'categories': final_categories,
                    'storages': final_storages
                })

            if name:
                recipes_1 = recipes.filter(name__icontains=name)
                categories_1 = categories.filter(name__icontains=name)
                storages_1 = storages.filter(name__icontains=name)

            if description:
                recipes_2 = recipes.filter(description__icontains=description)
                categories_2 = categories.filter(description__icontains=description)
                storages_2 = storages.filter(description__icontains=description)

            if name and description:
                final_recipes = list(chain(recipes_1, recipes_2))
                final_categories = list(chain(categories_1, categories_2))
                final_storages = list(chain(storages_1, storages_2))

            elif name and not description:
                final_recipes = recipes_1
                final_categories = categories_1
                final_storages = categories_1

            elif description and not name:
                final_recipes = recipes_2
                final_categories = categories_2
                final_storages = categories_2

            return render(request, 'recipes/name_search_results.html', {
                'recipes': final_recipes,
                'categories': final_categories,
                'storages': final_storages
            })
    else:
        form = SearchForm()
    return render(request, 'recipes/name_search.html', {'form': form})


def name_search_results(request):
    query = request.GET.get('query')  # Получите поисковый запрос
    recipes = Recipe.objects.filter(name__icontains=query)  # Получите результаты поиска
    context = {'recipes': recipes}  # Передайте результаты поиска в контекст шаблона
    return render(request, 'recipes/name_search_results.html', context)


def search_by_id(request, this_id=1):
    recipe = Recipe.objects.get(pk=this_id)
    return render(request, "recipes/search_by_id.html", {"item": recipe})

