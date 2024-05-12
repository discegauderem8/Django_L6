
from django.core.management.base import BaseCommand

from ... import models



class Command(BaseCommand):
    help = 'Изменяет существующего клиента'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Сustomer ID')

    def handle(self, *args, **kwargs):

        pk = kwargs.get("pk")
        client = models.Customer.objects.filter(pk=pk).first()

        client.name = input("Введите имя: ")
        client.email = input("Введите email: ")
        client.phone_number = int(input("Введите номер телефона: "))
        client.address = input("Введите адрес: ")

        client.save()

        self.stdout.write('Клиент успешно изменен')



# python manage.py update_client 1