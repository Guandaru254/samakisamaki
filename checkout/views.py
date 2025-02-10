from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart
from .forms import CheckoutForm
from decimal import Decimal

DELIVERY_FEE = Decimal('200.00')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty. Add items before checking out.")
        return redirect('cart')

    subtotal = sum(item.total_price() for item in cart_items)
    total_price = subtotal + DELIVERY_FEE

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            payment_method = request.POST.get('payment_method')

            # Create the order
            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                payment_method=payment_method,
                customer_name=f"{request.user.first_name} {request.user.last_name}",
                customer_phone=form.cleaned_data['mpesa_number'],
                delivery_address=form.cleaned_data['delivery_address'],
                delivery_city=form.cleaned_data['delivery_city'],
                delivery_postal_code=form.cleaned_data.get('delivery_postal_code', ''),
                special_instructions=form.cleaned_data.get('special_instructions', ''),
                status='Pending'
            )

            # Create order items from cart items
            order_items = [
                OrderItem(
                    order=order,
                    menu_item=cart_item.item,
                    quantity=cart_item.quantity
                )
                for cart_item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)  # More efficient than creating each item individually

            # Clear the user's cart
            cart_items.delete()

            messages.success(request, "Order placed successfully!")
            return redirect('order_success', order_id=order.id)
        else:
            messages.error(request, "There was an error with your checkout. Please check your details and try again.")

    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery_fee': DELIVERY_FEE,
        'total_price': total_price
    })


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'checkout/order_success.html', {'order': order})


def payment(request):
    return render(request, 'checkout/payment.html')