from django.db import models

from accounts.models import CustomUser

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses', limit_choices_to={'role': 'trainer'})

    def __str__(self):
        return self.title


class Payment(models.Model):
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments', limit_choices_to={'role': 'trainer'})
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trainer.email} - {self.amount}"