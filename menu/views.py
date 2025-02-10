from django.shortcuts import render, get_object_or_404
from .models import MenuItem
from cart.models import Cart  # Import your Cart model (ensure it exists)

def menu_list(request, category=None):
    category = request.GET.get('category')  # Handle category from query parameter
    search_query = request.GET.get('search')  # Handle search query
    min_price = request.GET.get('min_price')  # Minimum price filter
    max_price = request.GET.get('max_price')  # Maximum price filter
    sort_by = request.GET.get('sort_by')  # Sorting option
    cart_item_count = Cart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0  # Cart item count for authenticated users

    # Start with all menu items
    menu_items = MenuItem.objects.all()

    # Apply category filter
    if category:
        menu_items = menu_items.filter(category__iexact=category)  # Case-insensitive match

    # Apply search filter
    if search_query:
        menu_items = menu_items.filter(name__icontains=search_query)  # Case-insensitive partial match on name

    # Apply price range filter
    if min_price:
        menu_items = menu_items.filter(price__gte=min_price)
    if max_price:
        menu_items = menu_items.filter(price__lte=max_price)

    # Apply dietary preferences filters
    if 'vegetarian' in request.GET:
        menu_items = menu_items.filter(vegetarian=True)
    if 'gluten_free' in request.GET:
        menu_items = menu_items.filter(gluten_free=True)

    # Apply sorting
    if sort_by == 'price_asc':
        menu_items = menu_items.order_by('price')
    elif sort_by == 'price_desc':
        menu_items = menu_items.order_by('-price')
    elif sort_by == 'name_asc':
        menu_items = menu_items.order_by('name')
    elif sort_by == 'name_desc':
        menu_items = menu_items.order_by('-name')

    # Render the template with filtered and sorted menu items
    return render(request, 'menu/menu_list.html', {
        'menu_items': menu_items,
        'cart_item_count': cart_item_count,
        'category': category,
    })

def menu_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'menu/menu_detail.html', {'item': item})

def home(request):
    # Render the home page
    return render(request, 'home.html')