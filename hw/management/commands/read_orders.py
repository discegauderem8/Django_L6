from django.core.management.base import BaseCommand

from ... import models


class Command(BaseCommand):
    help = 'Читает созданные заказы'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        order = models.Order.objects.filter(pk=pk)

        self.stdout.write(f"{order}")

# python manage.py read_orders 2
