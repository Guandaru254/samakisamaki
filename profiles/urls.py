from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),  # Profile view
    path('profile/update/', views.update_profile, name='update_profile'),  # Update profile view
]