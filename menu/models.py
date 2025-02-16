from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Fixed ForeignKey issue
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name
