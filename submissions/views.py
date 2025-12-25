from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Submission
from .serializers import SubmissionSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Submission qo'shayotganda studentni hozirgi user qilib oladi
        serializer.save(student=self.request.user)
