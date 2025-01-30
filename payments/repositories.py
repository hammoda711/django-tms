from payments.models import Payment


class PaymentRepository:
    @staticmethod
    def create_payment(trainer, amount, status="Pending"):
        payment = Payment.objects.create(trainer=trainer, amount=amount, status=status)
        return payment

    @staticmethod
    def get_payments_for_trainer(trainer):
        return Payment.objects.filter(trainer=trainer)

    @staticmethod
    def get_payment_by_id(payment_id):
        return Payment.objects.filter(id=payment_id).first()

    @staticmethod
    def update_payment_status(payment, status):
        payment.status = status
        payment.save()
        return payment
