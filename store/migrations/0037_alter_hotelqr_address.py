# Generated by Django 4.2.4 on 2024-08-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0036_remove_hotelqr_restaurant_hotelqr_hotel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hotelqr",
            name="address",
            field=models.CharField(max_length=255, verbose_name="address"),
        ),
    ]