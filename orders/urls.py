from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),             # List all orders
    path('orders/create/<int:id>/', views.create_order, name='create_order'),  # Create a new order
    path('<int:pk>/', views.order_detail, name='order_detail'), # View order details
]
