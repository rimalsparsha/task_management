from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskRetrieveUpdateAPIViewTest(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        
        # Create a task for this user
        self.task = Task.objects.create(
            user=self.user,
            title="Sample Task",
            description="This is a sample task description.",
            completed=False
        )
        self.retrieve_update_url = reverse('task-Retrieve-update', args=[self.task.id])

    def test_retrieve_task_authenticated(self):
        # Retrieve the task details
        response = self.client.get(self.retrieve_update_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)
        self.assertEqual(response.data['description'], self.task.description)

    def test_retrieve_task_unauthenticated(self):
        # Log out to test unauthenticated access
        self.client.logout()
        response = self.client.get(self.retrieve_update_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_task_partial(self):
        # Update only the title of the task (partial update)
        response = self.client.patch(self.retrieve_update_url, {'title': 'Updated Task Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()  # Refresh from the database
        self.assertEqual(self.task.title, 'Updated Task Title')

    def test_update_task_full(self):
        # Full update of the task
        data = {
            'title': 'Fully Updated Task Title',
            'description': 'Updated task description',
            'completed': True
        }
        response = self.client.put(self.retrieve_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Fully Updated Task Title')
        self.assertEqual(self.task.description, 'Updated task description')
        self.assertTrue(self.task.completed)
