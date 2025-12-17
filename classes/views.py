from django.shortcuts import render
from rest_framework import generics
from .models import Classroom
from .serializers import ClassroomSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin


class ClassroomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated, IsAdmin]



class ClassroomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

