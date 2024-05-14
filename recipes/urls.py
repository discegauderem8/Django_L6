from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
from accounts.views import signup_view


urlpatterns = [
    path('', index, name='index'),
    path('name_search/', name_search, name='name_search'),
    path('search_results/', name_search_results, name='name_search_results'),
    path('search_by_id/<int:this_id>/', search_by_id, name='search_by_id'),
    path('search_cat_by_id/<int:this_id>/', search_cat_by_id, name='search_cat_by_id'),
    path('search_stor_by_id/<int:this_id>/', search_stor_by_id, name='search_stor_by_id'),

    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('storages/', StorageListView.as_view(), name='storage_list'),
    path('storages/create/', StorageCreateView.as_view(), name='storage_create'),
    path('storages/<int:pk>/edit/', StorageUpdateView.as_view(), name='storage_edit'),
    path('storages/<int:pk>/delete/', StorageDeleteView.as_view(), name='storage_delete'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]