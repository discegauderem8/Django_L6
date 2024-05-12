from django.core.management.base import BaseCommand

from ... import models


class Command(BaseCommand):
    help = 'Удаляет существующий заказ'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        order = models.Order.objects.filter(pk=pk).first()

        if order is not None:
            order.delete()

        self.stdout.write('Заказ успешно удален')

# python manage.py delete_order 1
