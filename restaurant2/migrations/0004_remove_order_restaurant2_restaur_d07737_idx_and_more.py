# Generated by Django 4.2.4 on 2024-06-17 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant2", "0003_remove_order_restaurant2_restaur_837b66_idx_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="order",
            name="restaurant2_restaur_d07737_idx",
        ),
        migrations.RemoveField(
            model_name="order",
            name="status",
        ),
        migrations.RemoveField(
            model_name="orderstatushistory",
            name="order",
        ),
        migrations.AddField(
            model_name="orderstatushistory",
            name="order_item",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="status_history",
                to="restaurant2.orderitem",
            ),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["restaurant"], name="restaurant2_restaur_837b66_idx"
            ),
        ),
    ]