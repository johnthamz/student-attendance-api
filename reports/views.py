from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from attendance.models import AttendanceRecord


class AttendanceReportAPIView(APIView):
    def get(self, request):
        data = AttendanceRecord.objects.values(
            'student__admission_number',
            'student__first_name',
            'status'
        )

        return Response(data)

