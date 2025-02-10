from django.db import models
from menu.models import MenuItem
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Tracks the user placing the order
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    special_instructions = models.TextField(blank=True, null=True)
    
    # Add delivery address fields # Provide default values for delivery fields
    delivery_address = models.TextField(default='Default Address')  # Complete address
    delivery_city = models.CharField(max_length=100, default='Unknown City')  # City
    delivery_postal_code = models.CharField(max_length=10, blank=True, null=True, default='00000')  # Postal Code# Postal Code (Optional)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"