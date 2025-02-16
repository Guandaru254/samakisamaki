# Generated by Django 5.1.6 on 2025-02-12 23:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("menu", "0002_remove_menuitem_available_menuitem_gluten_free_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("mpesa", "M-Pesa"), ("card", "Debit/Credit Card")],
                        max_length=10,
                    ),
                ),
                ("customer_name", models.CharField(max_length=100)),
                (
                    "customer_phone",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("delivery_address", models.TextField()),
                ("delivery_city", models.CharField(max_length=100)),
                (
                    "delivery_postal_code",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("special_instructions", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Processing", "Processing"),
                            ("Delivered", "Delivered"),
                            ("Canceled", "Canceled"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="checkout_orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.PositiveIntegerField()),
                (
                    "menu_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="menu.menuitem",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="checkout.order",
                    ),
                ),
            ],
        ),
    ]
