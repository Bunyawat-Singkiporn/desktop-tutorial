from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Full CRUD at /api/tasks/ — tighten permissions in Block D."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
