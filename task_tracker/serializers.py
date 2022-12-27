from rest_framework import serializers
from .models import Task_Tracker

class Task_TrackerSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Task_Tracker
    fields = ['id', 'task', 'description', 'is_done', 'created_date',]