from django.urls import path
from .views import (
    TrainerCreateView, TrainerRetrieveView, TrainerUpdateProfileView,
    TrainerUpdateAdminView, TrainerDeleteView, TrainerListView
)

urlpatterns = [
    path('create/', TrainerCreateView.as_view(), name='trainer-create'),
    path('<int:pk>/', TrainerRetrieveView.as_view(), name='trainer-retrieve'),
    path('<int:pk>/update-profile/', TrainerUpdateProfileView.as_view(), name='trainer-update-profile'),
    path('<int:pk>/update-admin/', TrainerUpdateAdminView.as_view(), name='admin-update-trainer-profile'),
    path('delete/<int:pk>/', TrainerDeleteView.as_view(), name='trainer-delete'),
    path('', TrainerListView.as_view(), name='trainer-list'),
]
