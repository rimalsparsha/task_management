from rest_framework import serializers
from .models import Task

# create task
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']