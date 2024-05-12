from django.urls import path

from . import views

urlpatterns = [
    path('', views.flip, name='index'),
    path('stats/', views.stats, name='stats'),
    # path('about/', views.about, name='about'),
]
