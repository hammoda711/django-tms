from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from payments.models import Payment
from trainers.models import Trainer

User = get_user_model()

class PaymentAPITestCase(APITestCase):
    
    def setUp(self):
        # Create an admin user
        self.admin_user = User.objects.create_superuser(email="admin@example.com", password="adminpass")
        self.admin_token = str(RefreshToken.for_user(self.admin_user).access_token)

        # Create a normal user
        self.user = User.objects.create_user(email="user@example.com", password="userpass", is_staff=False)
        self.user_token = str(RefreshToken.for_user(self.user).access_token)
        
        # Create a trainer user
        self.trainer_user = User.objects.create_user(email="trainer@example.com", password="trainerpass", is_staff=False)
        self.trainer = Trainer.objects.create(user=self.trainer_user, specialization="Fitness")
        
        # Create a payment for the trainer
        self.payment = Payment.objects.create(trainer=self.trainer, amount=100, status="Pending")

    def authenticate(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_payment_as_admin(self):
        self.authenticate(self.admin_token)
        data = {
            "trainer_id": self.trainer.id,
            "amount": 200,
            "status": "Pending"
        }
        response = self.client.post("/api/payments/create-payment/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["trainer"], self.trainer.id)
        self.assertEqual(response.data["amount"], "200.00")

    def test_create_payment_as_non_admin(self):
        self.authenticate(self.user_token)
        data = {
            "trainer_id": self.trainer.id,
            "amount": 200,
            "status": "Pending"
        }
        response = self.client.post("/api/payments/create-payment/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_list_payments_as_admin(self):
        self.authenticate(self.admin_token)
        response = self.client.get(f"/api/payments/trainer/{self.trainer.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_payments_as_trainer(self):
        self.authenticate(self.user_token)
        response = self.client.get(f"/api/payments/trainer/{self.trainer.id}/")
        self.assertEqual(response.status_code,  status.HTTP_200_OK)
    
    def test_update_payment_status_as_admin(self):
        self.authenticate(self.admin_token)
        data = {"status": "Completed"}
        response = self.client.patch(f"/api/payments/payment/{self.payment.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        self.assertEqual(self.payment.status, "Completed")

    def test_update_payment_status_as_non_admin(self):
        self.authenticate(self.user_token)
        data = {"status": "Completed"}
        response = self.client.patch(f"/api/payments/payment/{self.payment.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_update_payment_invalid_status(self):
        self.authenticate(self.admin_token)
        data = {"status": "InvalidStatus"}
        response = self.client.patch(f"/api/payments/payment/{self.payment.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
