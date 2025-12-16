from django.db import models
from classes.models import Classroom

class Student(models.Model):
    ACTIVE = 'active'
    TRANSFERRED = 'transferred'
    DROPPED = 'dropped'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (TRANSFERRED, 'Transferred'),
        (DROPPED, 'Dropped'),
    ]

    admission_number = models.CharField(
        max_length=20,
        primary_key=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)

    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )

    def __str__(self):
        return f"{self.admission_number} - {self.first_name} {self.last_name}"



class Enrollment(models.Model):
    ACTIVE = 'active'
    TRANSFERRED = 'transferred'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (TRANSFERRED, 'Transferred'),
        (COMPLETED, 'Completed'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )

    def __str__(self):
        return f"{self.student} → {self.classroom}"

