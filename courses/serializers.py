from rest_framework import serializers
from .models import Courses, Lesson

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'title', 'description', 'teacher', 'created_at')
        read_only_fields = ('teacher', 'created_at')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'course', 'title', 'video_url', 'created_at')
        read_only_fields = ('created_at',)