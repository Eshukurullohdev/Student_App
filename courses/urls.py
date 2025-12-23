from django.urls import path
from .views import CourseCreateView, CourseListView


urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('list/', CourseListView.as_view(), name='course-list'),
]
