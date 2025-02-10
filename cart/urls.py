from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),  # View cart
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # Add item to cart
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),  # Remove item from cart
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),  # Update item quantity
    path('cart/clear/', views.clear_cart, name='clear_cart'),  # Clear entire cart
]