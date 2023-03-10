from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.paid = True
        order.save()
        return render(request, 'payment/done.html', {'order': order})
    else:
        return render(request, 'payment/process.html', {'order': order})


def payment_done(request):
    return render(request, 'payment/done.html')


