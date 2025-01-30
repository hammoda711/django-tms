from django.urls import path
from .views import PaymentCreateView, PaymentListView, PaymentUpdateView

urlpatterns = [
    path('create-payment/', PaymentCreateView.as_view(), name='create-payment'),
    path('trainer/<int:trainer_id>/', PaymentListView.as_view(), name='list-payments'),
    path('payment/<int:payment_id>/update/', PaymentUpdateView.as_view(), name='update-payment'),
]
