from django.shortcuts import render
from rest_framework import generics
from .models import Courses
from .serializers import CourseSerializer
from .permissions import IsTeacher
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CourseCreateView(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class CourseListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]