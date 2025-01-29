# courses/serializers.py
from rest_framework import serializers

from trainers.serializers import LinkTrainerSerializer, TrainerSerializer
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    #trainers = TainerSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']

#link trainers to courses
class CourseTrainerSerializer(serializers.ModelSerializer):
    trainers = LinkTrainerSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description','trainers']
