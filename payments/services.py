from payments.repositories import PaymentRepository


class PaymentService:
    @staticmethod
    def create_payment_for_trainer(trainer, amount, status="Pending"):
        return PaymentRepository.create_payment(trainer, amount, status)

    @staticmethod
    def get_trainer_payments(trainer):
        return PaymentRepository.get_payments_for_trainer(trainer)

    @staticmethod
    def update_payment_status(payment, status):
        return PaymentRepository.update_payment_status(payment, status)
