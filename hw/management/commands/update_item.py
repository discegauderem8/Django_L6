
from django.core.management.base import BaseCommand

from ... import models



class Command(BaseCommand):
    help = 'Изменяет существующий товар'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')

    def handle(self, *args, **kwargs):

        pk = kwargs.get("pk")
        item = models.Item.objects.filter(pk=pk).first()

        item.name = input("Введите имя товара: ")
        item.description = input("Введите описание товара: ")
        item.price = int(input("Введите цену товара: "))
        item.count = int(input("Введите количество товара: "))

        item.save()

        self.stdout.write('Товар успешно изменен')



# python manage.py update_item 3
