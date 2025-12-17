from django.shortcuts import render
from rest_framework import generics
from .models import AttendanceSession, AttendanceRecord
from .serializers import AttendanceSessionSerializer, AttendanceRecordSerializer


class AttendanceSessionListCreateAPIView(generics.ListCreateAPIView):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer


class AttendanceSessionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer


class AttendanceRecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer


class AttendanceRecordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

