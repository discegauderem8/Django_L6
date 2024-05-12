from django.core.management.base import BaseCommand
from datetime import datetime
from random import randint
from ... import models


class Command(BaseCommand):
    help = 'Создаёт новый заказ. ID клиента передается в качестве аргумента в командной строке'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Сustomer ID')

    def handle(self, *args, **kwargs):

        pk = kwargs["pk"]

        items = list(map(int, input("Введите ID товаров через пробел: ").split()))

        count = 0

        for i in range(len(items)):
            item_count = int(input(f"Введите количество товара № {i + 1}: "))
            item_pk = items[i]
            this_item = models.Item.objects.filter(pk=item_pk).first()
            if this_item is None or this_item.count - item_count < 0:
                self.stdout.write("Товара нет в таком количестве на складе, он не будет внесен")
                items = [i for i in items if i != item_pk]
            else:
                count += item_count
                this_item.count -= item_count
                this_item.save()

        if count != 0:

            year = randint(2023,2025)
            month = randint(3,5)
            date = datetime(year, month, 16, 12, 30)
            order = models.Order(customer=models.Customer.objects.filter(pk=pk).first(), total_amount=count, created_at = date)

            order.save()

            for i in items:
                order.items.add(models.Item.objects.filter(pk=i).first())

            order.save()

            self.stdout.write('Заказ успешно создан')

        else:
            self.stdout.write("Заказ не был создан, так как в него не внесены товары")

# python manage.py new_order 1
# ID товара - 3
