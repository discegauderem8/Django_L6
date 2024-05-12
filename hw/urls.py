from django.urls import path
from .views import index, get_orders, create_customer, create_item, create_order, upload_image

urlpatterns = [
    path("", index, name="index"),
    path("orders/<int:user_id>/", get_orders, name="get_data"),
    path("semfour/customer", create_customer, name="new_customer"),
    path("semfour/item", create_item, name="new_item"),
    path("semfour/order", create_order, name="new_order"),
    path("semfour/upload/<int:item_id>", upload_image, name="upload_image")
]
