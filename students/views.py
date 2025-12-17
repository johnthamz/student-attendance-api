from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from .models import Enrollment
from .serializers import EnrollmentSerializer

from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'admission_number'
    permission_classes = [IsAuthenticated, IsAdmin]

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'admission_number'

class EnrollmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

