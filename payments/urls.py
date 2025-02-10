from django.urls import path
from . import views

urlpatterns = [
    path('stk-push/', views.stk_push, name='stk_push'),
    path('confirm-order/', views.confirm_order, name='confirm_order'),
    path('mpesa-callback/', views.mpesa_callback, name='mpesa_callback'),  # Optional callback endpoint
]