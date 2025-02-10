from django.urls import path
from . import views  # Import views from cart

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),  
]