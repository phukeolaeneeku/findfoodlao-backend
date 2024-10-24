# Generated by Django 4.2.4 on 2024-05-02 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0030_rename_title_noticemodel_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goodsmodel",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="store.categorymodel",
                verbose_name="category",
            ),
        ),
    ]