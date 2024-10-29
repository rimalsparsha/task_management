from django.urls import path
from .views import TaskCompletedAPIView, TaskCreateAPIView, TaskDeleteAPIView, TaskListAPIView, TaskRetrieveUpdateAPIView

urlpatterns = [
    # create tasks
    path('create-tasks/', TaskCreateAPIView.as_view(), name='task-create'),

    # list tasks of a specific user
    path('list-tasks/', TaskListAPIView.as_view(), name='list-create'),

    # Retrieve & Update task of a specific user
    path('retrieve-update-task/<int:id>/', TaskRetrieveUpdateAPIView.as_view(), name='task-Retrieve-update'),

    # Mark Task as Completed
    path('tasks/<int:id>/complete/', TaskCompletedAPIView.as_view(), name='task-complete'),

    # Delete task of a specific user
    path('delete-task/<int:id>/', TaskDeleteAPIView.as_view(), name='task-delete'),
    
]
