from datetime import datetime

import logging

from django.core.files.storage import FileSystemStorage
from django.utils.timezone import make_aware
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from django.views.generic import RedirectView
from django.urls import reverse
from django.utils.http import urlencode
from .forms import CustomerForm, ItemForm, OrderForm, ImageForm
from .models import Item, Order, Customer

# Create your views here.

logger = logging.getLogger(__name__)

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"Получили {form.cleaned_data}")
    else:
        form = CustomerForm()
    return render(request, 'hw/customer.html', {'form': form})



def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            text_data = form.cleaned_data
            new_item = Item(
                name=text_data['name'],
                description=text_data['description'],
                price=text_data['price'],
                count=text_data['count'],
            )
            logger.info(f"Получили {form.cleaned_data}")
            new_item.save()
            return render(request, "hw/success.html")

    else:
        form = ItemForm()

    return render(request, 'hw/item.html', {'form': form})



def upload_image(request, item_id):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            file_path = fs.url(filename)
            item = Item.objects.get(pk=item_id)
            item.image = file_path
            item.save()
            logger.info(f"Получили {form.cleaned_data}")
            return render(request, "hw/success.html")

    else:
        form = ImageForm()

    return render(request, "hw/upload_image.html", {"form": form})



def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data["customer"]
            items = form.cleaned_data["items"]
            total_amount = form.cleaned_data["total_amount"]
            new_order = Order(customer=customer, total_amount=total_amount)
            new_order.save()
            new_order.items.set(items)  #В случае с ManyToManyField можно задавать значения только через set()
            new_order.save()
            logger.info(f"Получили {form.cleaned_data}")
            return render(request, "hw/success.html")
    else:
        form = OrderForm()
    return render(request, 'hw/order.html', {'form': form})







def index(request):
    context = {"name": "Пользователь"}
    return render(request, "hw/index.html", context)


from datetime import datetime
from django.utils.timezone import make_aware
from django.shortcuts import render
from . import models

def get_orders(request, user_id):
    current_datetime = datetime.now()

    orders = models.Order.objects.filter(customer=user_id)

    years_threshold = make_aware(current_datetime.replace(year=2022))
    months_threshold = make_aware(current_datetime.replace(month=3))
    weeks_threshold = make_aware(current_datetime.replace(day=current_datetime.day-7))

    this_years_orders = orders.filter(created_at__gt=years_threshold).distinct()
    this_months_orders = orders.filter(created_at__gt=months_threshold).distinct()
    this_weeks_orders = orders.filter(created_at__gt=weeks_threshold).distinct()


    this_years_items = models.Item.objects.filter(order__in=this_years_orders).distinct()

    context = {
        "year_data": this_years_orders,
        "month_data": this_months_orders,
        "week_data": this_weeks_orders,
        "year_items": this_years_items
    }

    return render(request, "hw/orders.html", context=context)




