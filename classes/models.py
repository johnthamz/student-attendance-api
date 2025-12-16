from django.db import models

from accounts.models import TeacherProfile


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    class_teacher = models.OneToOneField(
        TeacherProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='classroom'
    )

    def __str__(self):
        return f"{self.level} - {self.name}"

