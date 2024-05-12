from django.contrib import admin

from .models import Customer, Order, Item


# Register your models here.


@admin.action(description="Cбросить количество до единицы")
def reset_count(modeladmin, request, queryset):
    queryset.update(count=1)


class CustomerAdmin(admin.ModelAdmin):
    fields = ["name", "email", "phone_number", "address", "created_at"]
    list_display = ["name", "email", "phone_number", "address", "created_at"]
    ordering = ["name"]
    list_filter = ["created_at", "name", "address"]
    search_fields = ["name", "address"]
    search_help_text = "Поиск по имени пользователя или адресу"


@admin.register(Item)  # То же самое, что admin.site.register(Item)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]
    actions = [reset_count]
    fieldsets = [
        (
            "Общая информация",
            {
                "fields": ["name", "count", "price"],
            },
        ),
        (
            "Подробности",
            {
                "classes": ["collapse"],
                "fields": ["description", "image"],
            },
        ),
        (
        "Дата добавления",
        {
            "fields" : ["created_at"]
        }
        )
    ]

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]
    fields = ["customer", "items", "total_amount", "created_at"]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
