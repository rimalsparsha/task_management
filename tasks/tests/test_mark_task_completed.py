from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskCompletedAPIViewTest(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        
        # Create a task for this user that is initially not completed
        self.task = Task.objects.create(
            user=self.user,
            title="Incomplete Task",
            description="This task is initially not completed.",
            completed=False
        )
        # Define the URL for marking the task as completed
        self.complete_url = reverse('task-complete', args=[self.task.id])

    def test_mark_task_completed_authenticated(self):
        # Send a PATCH request to mark the task as completed
        response = self.client.patch(self.complete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Refresh the task instance from the database and check completion status
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)  # Task should now be marked as completed
        self.assertEqual(response.data['completed'], True)  # Confirm in response data

    def test_mark_task_completed_unauthenticated(self):
        # Log out to test unauthenticated access
        self.client.logout()
        
        # Try to mark the task as completed without being authenticated
        response = self.client.patch(self.complete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
