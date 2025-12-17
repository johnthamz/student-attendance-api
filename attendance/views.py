from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AttendanceSession, AttendanceRecord
from .serializers import AttendanceSessionSerializer, AttendanceRecordSerializer
from accounts.permissions import IsTeacher



class AttendanceSessionListCreateAPIView(generics.ListCreateAPIView):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer
    permission_classes = [IsAuthenticated, IsTeacher]


class AttendanceSessionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer


class AttendanceRecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

class AttendanceRecordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

class BulkAttendanceAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def post(self, request):
        session_id = request.data.get('session')
        records = request.data.get('records', [])

        created = []

        for record in records:
            attendance = AttendanceRecord.objects.create(
                session_id=session_id,
                student_id=record['student'],
                status=record['status'],
                marked_by=request.user
            )
            created.append(attendance.id)

        return Response(
            {"message": "Attendance recorded successfully", "records": created},
            status=status.HTTP_201_CREATED
        )


