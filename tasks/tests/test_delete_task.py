from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskDeleteAPIViewTest(APITestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        
        # Create a task for this user
        self.task = Task.objects.create(
            user=self.user,
            title="Sample Task",
            description="This is a task to be deleted."
        )
        # Define the URL for deleting the task
        self.delete_url = reverse('task-delete', args=[self.task.id])

    def test_delete_task_authenticated(self):
        # Send a DELETE request to delete the task
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the task no longer exists in the database
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_delete_task_unauthenticated(self):
        # Log out to test unauthenticated access
        self.client.logout()
        
        # Try to delete the task without being authenticated
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Verify that the task still exists in the database
        self.assertTrue(Task.objects.filter(id=self.task.id).exists())
