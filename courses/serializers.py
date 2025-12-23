from rest_framework import serializers
from .models import Courses

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'title', 'description', 'teacher', 'created_at')
        read_only_fields = ('teacher', 'created_at')
