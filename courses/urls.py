from django.urls import path
from .views import CourseCreateView, CourseListView, CourseDetailView, LessonCreateView, LessonListView, AssignmentCreateView, AssignmentListView


urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('list/', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/',CourseDetailView.as_view(), name='course-detail'),
    path('<int:course_id>/lessons/', LessonListView.as_view()),
    path('lessons/create/', LessonCreateView.as_view()),
    path('<int:course_id>/assignments/', AssignmentListView.as_view()),
    path('assignments/create/', AssignmentCreateView.as_view()),
]
