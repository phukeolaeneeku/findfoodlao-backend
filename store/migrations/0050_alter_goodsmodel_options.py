# Generated by Django 4.2.4 on 2024-10-23 08:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0049_remove_bankaccount_image_bankaccount_image1_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="goodsmodel",
            options={
                "ordering": ["category__name"],
                "verbose_name_plural": "3. Product list",
            },
        ),
    ]
