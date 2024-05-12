from django.core.management.base import BaseCommand

from ... import models


class Command(BaseCommand):
    help = 'Создаёт нового клиента'

    def handle(self, *args, **kwargs):
        name = input("Введите имя: ")
        email = input("Введите email: ")
        phone_number = int(input("Введите номер телефона: "))
        address = input("Введите адрес: ")

        customer = models.Customer(name=name, email=email, phone_number=phone_number, address=address)
        customer.save()

        self.stdout.write('Клиент успешно создан')

# python manage.py new_client
