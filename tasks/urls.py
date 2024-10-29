from django.urls import path
from .views import TaskCreateView

urlpatterns = [
    # create tasks
    path('create-tasks/', TaskCreateView.as_view(), name='task-create'),
]
