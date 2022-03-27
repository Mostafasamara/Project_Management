from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    # created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = '__all__'
