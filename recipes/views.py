from itertools import chain

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from .forms import RecipeForm, CategoryForm, StorageForm, SearchForm, SignUpForm
from .models import Recipe, Category, Storage


def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def index(request):
    recipes = Recipe.objects.all().order_by('?')[:5]
    return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
def name_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            this_id = form.cleaned_data.get('id')
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            search_recipes = form.cleaned_data.get('recipe_check')
            search_categories = form.cleaned_data.get('category_check')
            search_storages = form.cleaned_data.get('storage_check')

            recipes = Recipe.objects.all()
            categories = Category.objects.all()
            storages = Storage.objects.all()
            if this_id:
                final_recipes = recipes.filter(pk=this_id) if search_recipes else None
                final_categories = categories.filter(pk=this_id) if search_categories else None
                final_storages = storages.filter(pk=this_id) if search_storages else None

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
                final_recipes = list(chain(recipes_1, recipes_2)) if search_recipes else None
                final_categories = list(chain(categories_1, categories_2)) if search_categories else None
                final_storages = list(chain(storages_1, storages_2)) if search_storages else None

            elif name and not description:
                final_recipes = recipes_1 if search_recipes else None
                final_categories = categories_1 if search_categories else None
                final_storages = storages_1 if search_storages else None

            elif description and not name:
                final_recipes = recipes_2 if search_recipes else None
                final_categories = categories_2 if search_categories else None
                final_storages = storages_2 if search_storages else None

            return render(request, 'recipes/name_search_results.html', {
                'recipes': final_recipes,
                'categories': final_categories,
                'storages': final_storages
            })
    else:
        form = SearchForm()
    return render(request, 'recipes/name_search.html', {'form': form})

@login_required
def name_search_results(request):
    query = request.GET.get('query')
    recipes = Recipe.objects.filter(name__icontains=query)
    context = {'recipes': recipes}
    return render(request, 'recipes/name_search_results.html', context)

@login_required
def search_by_id(request, this_id):
    recipe = get_object_or_404(Recipe, pk=this_id)
    return render(request, "recipes/search_by_id.html", {"item": recipe})

@login_required
def search_cat_by_id(request, this_id):
    category = get_object_or_404(Category, pk=this_id)
    return render(request, "recipes/search_cat_by_id.html", {"item": category})

@login_required
def search_stor_by_id(request, this_id):
    storage = get_object_or_404(Storage, pk=this_id)
    return render(request, "recipes/search_stor_by_id.html", {"item": storage})

# Recipe views
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')

# Category views
class CategoryListView(ListView):
    model = Category
    template_name = 'recipes/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'recipes/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'recipes/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'recipes/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

# Storage views
class StorageListView(ListView):
    model = Storage
    template_name = 'recipes/storage_list.html'
    context_object_name = 'storages'

class StorageCreateView(CreateView):
    model = Storage
    form_class = StorageForm
    template_name = 'recipes/storage_form.html'
    success_url = reverse_lazy('storage_list')

class StorageUpdateView(UpdateView):
    model = Storage
    form_class = StorageForm
    template_name = 'recipes/storage_form.html'
    success_url = reverse_lazy('storage_list')

class StorageDeleteView(DeleteView):
    model = Storage
    template_name = 'recipes/storage_confirm_delete.html'
    success_url = reverse_lazy('storage_list')
