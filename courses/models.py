from django.db import models
from trainers.models import Trainer
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    trainers = models.ManyToManyField(Trainer, related_name='courses', limit_choices_to={'role': 'trainer'})

    def __str__(self):
        return self.title

