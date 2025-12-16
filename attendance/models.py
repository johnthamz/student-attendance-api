from django.db import models
from classes.models import Classroom
from students.models import Student
from accounts.models import User


class AttendanceSession(models.Model):
    MORNING = 'morning'
    AFTERNOON = 'afternoon'

    SESSION_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
    ]

    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='attendance_sessions'
    )
    date = models.DateField()
    session_type = models.CharField(
        max_length=20,
        choices=SESSION_CHOICES
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.classroom} - {self.date} ({self.session_type})"


class AttendanceRecord(models.Model):
    PRESENT = 'present'
    ABSENT = 'absent'

    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
    ]

    session = models.ForeignKey(
        AttendanceSession,
        on_delete=models.CASCADE,
        related_name='records'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    marked_at = models.DateTimeField(auto_now_add=True)
    marked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{self.student} - {self.status}"
