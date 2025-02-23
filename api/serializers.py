from rest_framework.serializers import ModelSerializer
from api.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'deleted_at']