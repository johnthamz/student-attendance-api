from django.urls import path
from .views import AttendanceReportAPIView

urlpatterns = [
    path('reports/attendance/', AttendanceReportAPIView.as_view(), name='attendance-report'),
]

