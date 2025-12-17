from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from attendance.models import AttendanceRecord
from attendance.serializers import AttendanceRecordSerializer


class AttendanceReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        records = AttendanceRecord.objects.all()
        serializer = AttendanceRecordSerializer(records, many=True)
        return Response(serializer.data)


