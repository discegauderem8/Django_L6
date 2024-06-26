# Generated by Django 5.0.4 on 2024-05-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hw", "0004_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_amount",
            field=models.PositiveIntegerField(),
        ),
    ]
