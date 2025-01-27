from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Payment(models.Model):
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='trainer_payments', limit_choices_to={'role': 'trainer'})
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name