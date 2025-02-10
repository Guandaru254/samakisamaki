from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),          # List all reviews
    path('create/', views.create_review, name='create_review'), # Create a new review
    path('<int:pk>/', views.review_detail, name='review_detail'), # View review details
]