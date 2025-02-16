from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),  # Main menu list
    path('menu_list/', views.menu_list, name='menu_list_page'),
    path('menu/<int:item_id>/', views.menu_detail, name='menu_detail'),  # Menu item detail (higher priority)
    path('menu/category/<str:category>/', views.menu_list, name='menu_list_category'),  # Category-specific menu list
]