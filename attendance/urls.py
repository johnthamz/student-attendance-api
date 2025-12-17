from django.urls import path

from .views import (
    AttendanceSessionListCreateAPIView,
    AttendanceSessionDetailAPIView,
    AttendanceRecordListCreateAPIView,
    AttendanceRecordDetailAPIView,
)
from .views import BulkAttendanceAPIView

urlpatterns = [
    path('attendance-sessions/', AttendanceSessionListCreateAPIView.as_view(), name='attendance-session-list-create'),
    path('attendance-sessions/<int:pk>/', AttendanceSessionDetailAPIView.as_view(), name='attendance-session-detail'),

    path('attendance-records/', AttendanceRecordListCreateAPIView.as_view(), name='attendance-record-list-create'),
    path('attendance-records/<int:pk>/', AttendanceRecordDetailAPIView.as_view(), name='attendance-record-detail'),
]

urlpatterns += [
    path('attendance/bulk/', BulkAttendanceAPIView.as_view(), name='bulk-attendance'),
]