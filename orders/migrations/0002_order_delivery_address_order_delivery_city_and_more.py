# Generated by Django 5.0.3 on 2025-01-30 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="delivery_address",
            field=models.TextField(default="Default Address"),
        ),
        migrations.AddField(
            model_name="order",
            name="delivery_city",
            field=models.CharField(default="Unknown City", max_length=100),
        ),
        migrations.AddField(
            model_name="order",
            name="delivery_postal_code",
            field=models.CharField(
                blank=True, default="00000", max_length=10, null=True
            ),
        ),
    ]
