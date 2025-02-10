from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Cart
from menu.models import MenuItem

# Display the cart
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    # Calculate subtotal
    subtotal = sum(item.total_price() for item in cart_items)
    delivery_fee = 200  # Fixed delivery fee
    total_price = subtotal + delivery_fee  # Grand total

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'total_price': total_price
    })


# Add item to cart
@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, item=item)

    if not created:
        cart_item.quantity += 1  # If already in cart, increase quantity
        cart_item.save()

    messages.success(request, f"{item.name} added to cart.")
    return redirect('menu_list')  # Redirect to the menu page


# Remove item from cart
@login_required
def cart_remove(request, item_id):
    cart_item = get_object_or_404(Cart, user=request.user, id=item_id)
    cart_item.delete()

    messages.success(request, "Item removed from your cart.")
    return redirect('cart_view')


# Update quantity of an item in cart
@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(Cart, user=request.user, item_id=item_id)

    if request.method == 'POST':
        try:
            new_quantity = int(request.POST.get('quantity', 1))
            if new_quantity > 0:
                cart_item.quantity = new_quantity
                cart_item.save()
            else:
                cart_item.delete()

            # Recalculate totals
            cart_items = Cart.objects.filter(user=request.user)
            subtotal = sum(item.total_price() for item in cart_items)
            delivery_fee = 200
            total_price = subtotal + delivery_fee

            # Return updated totals as JSON
            return JsonResponse({
                "item_total": cart_item.total_price(),
                "subtotal": subtotal,
                "total_price": total_price
            })
        except (ValueError, TypeError):
            return HttpResponseBadRequest("Invalid quantity value.")

    return redirect('cart_view')


# Clear entire cart
@login_required
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    messages.success(request, "Cart cleared successfully.")
    return redirect('cart_view')