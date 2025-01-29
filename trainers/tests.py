from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from trainers.models import Trainer
from trainers.repositories import TrainerRepository
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

class TrainerViewTests(APITestCase):
    def setUp(self):
        # Create admin user
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com", password="adminpass"
        )
        self.admin_token = str(AccessToken.for_user(self.admin_user))

        # Create regular user
        self.user = User.objects.create_user(email="user@example.com", password="userpass")
        self.user_token = str(AccessToken.for_user(self.user))

        # Ensure user is not already a trainer
        if not Trainer.objects.filter(user=self.user).exists():
            self.trainer = TrainerRepository.create_trainer(self.user, specialization="Fitness")

        # URLs
        self.create_url = "/api/trainers/create/"
        self.retrieve_url = f"/api/trainers/{self.trainer.id}/"
        self.update_profile_url = f"/api/trainers/{self.trainer.id}/update-profile/"
        self.update_admin_url = f"/api/trainers/{self.trainer.id}/update-admin/"
        self.delete_url = f"/api/trainers/delete/{self.trainer.id}/"
        self.list_url = "/api/trainers/"

    def tearDown(self):
        Trainer.objects.all().delete()
        User.objects.all().delete()

    def test_admin_can_create_trainer(self):
        new_user = User.objects.create_user(email="newuser@example.com", password="newpass")
        data = {"user": new_user.email, "specialization": "Yoga"}
        response = self.client.post(self.create_url, data, HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_admin_cannot_create_trainer(self):
        data = {"user": self.user.email, "specialization": "Yoga"}
        response = self.client.post(self.create_url, data, HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_retrieve_any_trainer(self):
        response = self.client.get(self.retrieve_url, HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_trainer_can_retrieve_own_profile(self):
        response = self.client.get(self.retrieve_url, HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_other_trainer_profile(self):
        other_user = User.objects.create_user(email="other@example.com", password="otherpass")
        other_token = str(AccessToken.for_user(other_user))
        response = self.client.get(self.retrieve_url, HTTP_AUTHORIZATION=f"Bearer {other_token}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_trainer_can_update_own_profile(self):
        data = {"bio": "Updated bio"}
        response = self.client.patch(self.update_profile_url, data, HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_can_update_trainer_restricted_fields(self):
        data = {"specialization": "Updated Specialization"}
        response = self.client.patch(self.update_admin_url, data, HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_admin_cannot_update_trainer_restricted_fields(self):
        data = {"specialization": "Updated Specialization"}
        response = self.client.patch(self.update_admin_url, data, HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_delete_trainer(self):
        response = self.client.delete(self.delete_url, HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_admin_cannot_delete_trainer(self):
        response = self.client.delete(self.delete_url, HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_list_trainers(self):
        response = self.client.get(self.list_url, HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_admin_cannot_list_trainers(self):
        response = self.client.get(self.list_url, HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
