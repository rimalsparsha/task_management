from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from tasks.serializers import TaskCreateSerializer, TaskListSerializer
from tasks.models import Task
# Create your views here.

# Create Task
class TaskCreateAPIView(generics.CreateAPIView):
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
    


# List and Create View
class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed', 'title'] # Define the fields on which filtering is allowed
    # Set permission classes to ensure that only authenticated users can access
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return tasks that belong to the authenticated user
        return Task.objects.filter(user=self.request.user)
    

# Retrieve & Update Task
class TaskRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        # Check if it's a partial update; set to True by default
        partial = kwargs.pop('partial', True)  
        # Get the task instance that is to be updated
        instance = self.get_object()  
        # Create a serializer instance for the task with the new data
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # Validate the incoming data and raise an exception if invalid
        serializer.is_valid(raise_exception=True)
        # Save the updates to the task
        self.perform_update(serializer)  
        # Return the updated task data and a status code of 200 OK
        return Response(serializer.data, status=status.HTTP_200_OK)



# Mark Task as Completed
class TaskCompletedAPIView(generics.UpdateAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the task instance
        instance.completed = True  # Mark the task as completed
        instance.save()  # Save the updated task instance
        serializer = self.get_serializer(instance)  # Serialize the updated task
        return Response(serializer.data, status=status.HTTP_200_OK)



# Delete Task
class TaskDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)