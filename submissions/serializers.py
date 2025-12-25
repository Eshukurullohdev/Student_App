from rest_framework import serializers
from .models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)  # faqat username ko‘rsatadi
    assignment = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'student', 'file', 'submitted_at', 'grade']
