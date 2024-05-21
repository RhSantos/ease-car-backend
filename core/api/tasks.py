from background_task import background
from .models import Payment

@background(schedule=5)
def confirm_booking_payment(payment_id:str):
    payment = Payment.objects.get(id=payment_id)
    payment.payment_status = Payment.PaymentStatus.COMPLETED

    payment.save()