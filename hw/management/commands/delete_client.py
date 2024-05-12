
from django.core.management.base import BaseCommand

from ... import models



class Command(BaseCommand):
    help = 'Удаляет существующего клиента'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Сustomer ID')

    def handle(self, *args, **kwargs):

        pk = kwargs.get("pk")
        client = models.Customer.objects.filter(pk=pk).first()

        if client is not None:
            client.delete()


        self.stdout.write('Клиент успешно удален')


# python manage.py delete_client 1