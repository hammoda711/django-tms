from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from trainers.permissions import IsOwnerOrAdmin, IsTrainerOwner
from .models import Trainer
from .serializers import TrainerSerializer
from .services import TrainerService
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.exceptions import NotFound,PermissionDenied

class TrainerCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        user_email = request.data.get('user')  # Now expecting user email
        specialization = request.data.get('specialization')

        try:
            # Call the service to create the trainer
            trainer = TrainerService.create_trainer(user_email, specialization)
            return Response(TrainerSerializer(trainer).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            # Return a 400 Bad Request response with the error message
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#Retrieve Trainer (Owner or Admin)
class TrainerRetrieveView(generics.RetrieveAPIView):
    serializer_class = TrainerSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_object(self):
        trainer_id = self.kwargs.get("pk")
        # Retrieve trainer object based on the ID from the URL
        trainer = TrainerService.get_trainer_by_id(trainer_id)

        # If the trainer is not found, raise an error
        if not trainer:
            raise NotFound(f"Trainer with id {trainer_id} not found.")
        
        # Check if the logged-in user is allowed to access this trainer's profile
        # If the user is admin, they can retrieve any trainer profile
        if self.request.user.is_staff:
            return trainer

        # If the logged-in user is a trainer, only allow access to their own profile
        if trainer.user.id == self.request.user.id:
            return trainer
        
        # If the user is not an admin and not the owner, deny permission
        raise PermissionDenied("You do not have permission to access this trainer's profile.")
# 3. Update Trainer (Owner - Profile Fields)
class TrainerUpdateProfileView(generics.UpdateAPIView):
    """
    Allows trainers to update their profile only if the trainer ID in the URL matches their own trainer ID.
    """
    serializer_class = TrainerSerializer
    permission_classes = [IsTrainerOwner]

    def get_object(self):
        trainer_id = self.kwargs.get("pk")
        trainer = get_object_or_404(Trainer, id=trainer_id)

        # Ensure that the logged-in trainer can only update their own profile
        if trainer.user.id != self.request.user.id:
            raise PermissionDenied("You do not have permission to update this trainer's profile.")
        return trainer

    def patch(self, request, *args, **kwargs):
        trainer = self.get_object()
        updated_trainer = TrainerService.update_trainer_profile(trainer, request.data)
        return Response(TrainerSerializer(updated_trainer).data)

# 4. Update Trainer (Admin - Restricted Fields)
class TrainerUpdateAdminView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        trainer = get_object_or_404(Trainer, id=pk)
        updated_trainer = TrainerService.update_trainer_admin(trainer, request.data)
        return Response(TrainerSerializer(updated_trainer).data)

# 5. Delete Trainer (Admin Only)
class TrainerDeleteView(generics.DestroyAPIView):
    queryset = Trainer.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        trainer = get_object_or_404(Trainer, id=pk)
        TrainerService.delete_trainer(trainer)
        return Response({"detail": "Trainer deleted successfully"})

class TrainerListView(generics.ListAPIView):
    serializer_class = TrainerSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return TrainerService.list_all_trainers()
