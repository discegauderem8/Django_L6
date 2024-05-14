from django.db import models
from django.db.models import ManyToManyField


# Create your models here.

# class Recipe(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)
#     guide = models.CharField(max_length=10000)
#     timing = models.DecimalField(max_digits=10, decimal_places=2)
#     author = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="images/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)
#
#
# class Storage(models.Model):
#     name = models.CharField(max_length=200)
#     items = ManyToManyField(Recipe)
#     categories = ManyToManyField(Category)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    guide = models.CharField(max_length=10000)
    timing = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recipe: {self.name}, Description: {self.description}, Guide: {self.guide}, Timing: {self.timing}, Author: {self.author}, Image: {self.image}, Created at: {self.created_at}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"Category: {self.name}, Description: {self.description}"

class Storage(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(Recipe)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        items_list = ', '.join([item.name for item in self.items.all()])
        categories_list = ', '.join([category.name for category in self.categories.all()])
        return f"Storage: {self.name}, Items: {items_list}, Categories: {categories_list}"

