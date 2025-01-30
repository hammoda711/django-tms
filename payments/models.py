from django.db import models
from courses.models import Course
from trainers.models import Trainer

# Create your models here.
class Payment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending'
    )

    def __str__(self):
        return f"Payment to {self.trainer.full_name}"