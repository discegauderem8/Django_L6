from django.core.management.base import BaseCommand

from ... import models


class Command(BaseCommand):
    help = 'Удаляет существующий товар'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        item = models.Item.objects.filter(pk=pk).first()

        if item is not None:
            item.delete()

        self.stdout.write('Товар успешно удален')

# python manage.py delete_item 1
