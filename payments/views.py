from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.exceptions import NotFound
from trainers.permissions import IsOwnerOrAdmin
from trainers.repositories import TrainerRepository
from .serializers import PaymentSerializer
from .services import PaymentService
from .repositories import PaymentRepository


class PaymentCreateView(APIView):
    """
    Create a payment for a trainer.
    Only admin users can create a payment.
    """
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        trainer_id = request.data.get('trainer_id')
        amount = request.data.get('amount')
        status = request.data.get('status', 'Pending')

        # Use the TrainerRepository to get the trainer
        trainer = TrainerRepository.get_by_id(trainer_id)
        if not trainer:
            raise NotFound("Trainer not found.")

        # Create payment using the service
        payment = PaymentService.create_payment_for_trainer(trainer, amount, status)
        return Response(PaymentSerializer(payment).data, status=HTTP_201_CREATED)


class PaymentListView(APIView):
    """
    List all payments made to a specific trainer.
    Only admin users can view payments.
    """
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request, trainer_id, *args, **kwargs):
        # Use the TrainerRepository to get the trainer
        trainer = TrainerRepository.get_by_id(trainer_id)
        if not trainer:
            raise NotFound("Trainer not found.")

        # Get payments using the service
        payments = PaymentService.get_trainer_payments(trainer)
        return Response(PaymentSerializer(payments, many=True).data, status=HTTP_200_OK)


class PaymentUpdateView(APIView):
    """
    Update payment status (e.g., change from Pending to Completed).
    Only admin users can update payment status.
    """
    permission_classes = [IsAdminUser]

    def patch(self, request, payment_id, *args, **kwargs):
        # Use the PaymentRepository to get the payment
        payment = PaymentRepository.get_payment_by_id(payment_id)
        if not payment:
            raise NotFound("Payment not found.")

        # Update payment status
        status = request.data.get('status')
        if status not in ['Pending', 'Completed']:
            return Response({"detail": "Invalid status."}, status=400)

        updated_payment = PaymentService.update_payment_status(payment, status)
        return Response(PaymentSerializer(updated_payment).data, status=HTTP_200_OK)

