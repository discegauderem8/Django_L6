from django.conf.urls.static import static
from django.urls import path

from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_storage/', views.create_storage, name='create_storage'),
    path('name_search/', views.name_search, name='name_search'),
    path('items/<str:model_name>/', views.show_items, name='show_items'),
    path('search_results/', views.name_search_results, name='name_search_results'),  # Добавленный путь для отображения результатов поиска
]

