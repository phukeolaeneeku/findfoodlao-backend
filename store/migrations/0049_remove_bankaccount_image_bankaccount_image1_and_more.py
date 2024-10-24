# Generated by Django 4.2.4 on 2024-10-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0048_webinfo_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bankaccount",
            name="image",
        ),
        migrations.AddField(
            model_name="bankaccount",
            name="image1",
            field=models.FileField(
                blank=True, null=True, upload_to="media/", verbose_name="image1"
            ),
        ),
        migrations.AddField(
            model_name="bankaccount",
            name="image2",
            field=models.FileField(
                blank=True, null=True, upload_to="media/", verbose_name="image2"
            ),
        ),
    ]