# Generated by Django 4.2.4 on 2024-10-23 04:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0046_webinfo_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="webinfo",
            name="message",
        ),
    ]
