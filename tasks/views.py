from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from tasks.serializers import TaskCreateSerializer
from tasks.models import Task
# Create your views here.

# Create Task
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer
    # Set permission classes to ensure that only authenticated users can access
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Create an instance of the serializer with the incoming request data
        serializer = self.get_serializer(data=request.data)
        # Validate the incoming data
        serializer.is_valid(raise_exception=True)
        # Save the task with the authenticated user
        task = serializer.save(user=request.user)
        # Serialize the saved task instance to prepare the response data
        response_serializer = TaskCreateSerializer(task)
        # Return a response with the serialized task data and a status code of 201 Created
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)