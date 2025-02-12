from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from menu.views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Root URL redirects to login page
    path('', RedirectView.as_view(url='login/', permanent=True)),
    
    # Application-specific URLs
    path('menu/', include('menu.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('reviews/', include('reviews.urls')),
    path('home/', home, name='home'),
    path('cart/', include('cart.urls')),
    path('profile/', include('profiles.urls')),
    path('checkout/', include('checkout.urls')),
    path('gallery/', include('gallery.urls')),
    path('payments/', include('payments.urls')),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]

# Media files handling
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    from django.views.static import serve
    from django.urls import re_path

    # Serve media files in production if needed
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]