from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 'admin'
    TEACHER = 'teacher'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=TEACHER
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': User.TEACHER}
    )
    staff_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username} - Teacher"

