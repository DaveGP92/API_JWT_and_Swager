from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from serializers import TaskSerializer
from models import Task

@extend_schema_view(
    list= extend_schema(description = 'Permite obtener una lista de tareas'),
    retrieve= extend_schema(description = 'Permite obtener una tarea en específico'),
    create= extend_schema(description = 'Permite crear una tarea'),
    update= extend_schema(description= 'Permite actualziar una tarea'),
    destroy= extend_schema(description= 'Permite eliminar una tarea'),
)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer