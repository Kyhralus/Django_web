# # order/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Order, OrderItem
# from .forms import OrderCreateForm
# from DjangoWebApps.cart.cart import Cart # 从DjangoWebApps/cart/cart.py导入Cart类
#
# def order_create(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.user = request.user
#             order.save()
#
#             for item in cart:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item['product'],
#                     price=item['price'],
#                     quantity=item['quantity']
#                 )
#
#             cart.clear()
#             return redirect('order:order_detail', order.id)
#     else:
#         form = OrderCreateForm()
#
#     return render(request, 'order/order_create.html', {'cart': cart, 'form': form})
#
# @login_required
# def order_list(request):
#     orders = Order.objects.filter(user=request.user)
#     return render(request, 'order/order_list.html', {'orders': orders})
#
# @login_required
# def order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     return render(request, 'order/order_detail.html', {'order': order})