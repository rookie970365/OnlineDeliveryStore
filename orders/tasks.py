from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from orders.models import Order


@shared_task
def notify_order_created(order_id):
    order = Order.objects.get(id=order_id)
    status = "paid" if order.paid else "Pending payment"
    message = (
        f"Your order {order_id} has been successfully completed\n"
        f"Created at {order.created}\n"
        f"Customer {order.first_name} {order.last_name}\n"
        f"E-mail {order.email}\n"
        f"Status {status}"
        "\n\n"
        # f"Check order at: {settings.BASE_URL}{path}"
        f"Sincerely,\nYour admin."
    )
    send_mail(
        subject=f"New order No.{order_id}",
        message=message,
        from_email="brew_bros@example.com",
        recipient_list=[order.email, ],
    )
    return True
