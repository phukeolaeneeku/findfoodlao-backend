# Generated by Django 4.2.4 on 2024-03-12 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_remove_goodsmodel_is_popular_categorymodel_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SizeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="size",
                        to="store.goodsmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ColorModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="color",
                        to="store.goodsmodel",
                    ),
                ),
            ],
        ),
    ]