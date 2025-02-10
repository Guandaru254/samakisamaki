# menu/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/')
    category = models.CharField(max_length=100, choices=(
        ('starters', 'Starters'),
        ('main_courses', 'Main Courses'),
        ('desserts', 'Desserts'),
        ('beverages', 'Beverages'),
        ('seafood', 'Seafood'),
        ('specials', 'Specials'),
    ))
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name