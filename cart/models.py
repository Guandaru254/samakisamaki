from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')  # Ensure a user can't have duplicate items in the cart
        ordering = ['-added_at']  # Most recently added items appear first

    def total_price(self):
        """Calculate total price for this cart item."""
        return self.item.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.quantity} x {self.item.name}"