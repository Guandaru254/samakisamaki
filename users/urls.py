from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),       # User registration
    path('login/', views.login_user, name='login'),           # User login
    path('logout/', views.logout_user, name='logout'),        # User logout
]