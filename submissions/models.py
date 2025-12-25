from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from courses.models import Assignment  # course app ichidagi Assignment modelini import qilamiz

class Submission(models.Model):
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    file = models.FileField(upload_to='submissions/')  # student fayl yuklaydi
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)  # o'qituvchi baho qo'yishi mumkin

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"
