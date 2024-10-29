from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import Task
from django.contrib.auth.models import User

class TaskListAPIViewTest(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a couple of tasks for the user
        self.task1 = Task.objects.create(user=self.user, title='Test Task 1', description='Description for task 1')
        self.task2 = Task.objects.create(user=self.user, title='Test Task 2', description='Description for task 2')
        self.url = reverse('list-create')  # URL for the list tasks endpoint

    def test_list_tasks_authenticated(self):
        # Authenticate the user
        self.client.login(username='testuser', password='testpass')
        
        # Send a GET request to the list tasks endpoint
        response = self.client.get(self.url)
        
        # Assert the response status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return two tasks
        self.assertEqual(response.data[0]['title'], self.task1.title)  # Check first task title
        self.assertEqual(response.data[1]['title'], self.task2.title)  # Check second task title

    def test_list_tasks_unauthenticated(self):
        # Send a GET request to the list tasks endpoint without authentication
        response = self.client.get(self.url)
        
        # Assert the response status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Should return 403 Forbidden
