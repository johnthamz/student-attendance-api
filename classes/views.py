from django.shortcuts import render
from rest_framework import generics
from .models import Classroom
from .serializers import ClassroomSerializer


class ClassroomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

