from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task


# Create your tests here.
class TaskCreateAPIViewTest(APITestCase):
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Define the URL for the task creation endpoint
        self.url = reverse('task-create')
    
    def test_create_task_success(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Define the payload for creating a task
        data = {
            'title': 'Test Task',
            'description': 'This is a test task.'
        }
        
        # Make the POST request to create a task
        response = self.client.post(self.url, data, format='json')
        
        # Assert that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that the task is created in the database
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')
    
    def test_create_task_unauthenticated(self):
        # Attempt to create a task without logging in
        data = {
            'title': 'Unauthenticated Task',
            'description': 'This task should not be created.'
        }
        
        response = self.client.post(self.url, data, format='json')
        
        # Assert that the response status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Assert that no tasks are created
        self.assertEqual(Task.objects.count(), 0)

    def test_create_task_invalid_data(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Define invalid payload (missing title)
        data = {
            'description': 'This task should fail due to missing title.'
        }
        
        response = self.client.post(self.url, data, format='json')
        
        # Assert that the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Assert that no tasks are created
        self.assertEqual(Task.objects.count(), 0)