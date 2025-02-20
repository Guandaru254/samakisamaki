from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu_list')  # Redirect to menu list on successful login
    else:
        form = AuthenticationForm()  # Create a new AuthenticationForm instance
    return render(request, 'users/login.html', {'form': form})  # Render login form on GET request

def logout_user(request):
    logout(request)
    return redirect('login')  # Redirects user to login page after logging out

# Password Reset View
class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
