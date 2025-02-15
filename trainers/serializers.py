# courses/serializers.py
from rest_framework import serializers
from .models import Trainer

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__' 
        read_only_fields = ['user']
         
#link trainers to courses
class LinkTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields =['id','full_name']