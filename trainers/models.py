from django.db import models

from accounts.models import CustomUser

# Create your models here.
from django.db import models
from accounts.models import CustomUser

class Trainer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)   
    profile_picture = models.ImageField(upload_to='trainers/profile_pics/', null=True, blank=True)
    specialization = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    total_sessions = models.PositiveIntegerField(default=0)
    feedback_score = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)   
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.specialization}'
