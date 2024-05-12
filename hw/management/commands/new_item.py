from django.core.management.base import BaseCommand

from ... import models


class Command(BaseCommand):
    help = 'Создаёт новый товар'

    def handle(self, *args, **kwargs):
        name = input("Введите имя товара: ")
        description = input("Введите описание: ")
        price = int(input("Введите цену: "))
        count = input("Введите количество: ")

        item = models.Item(name=name, description=description, price=price, count=count)
        item.save()

        self.stdout.write('Товар успешно создан')

# python manage.py new_item
