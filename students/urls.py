from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView
from .views import (
    StudentListCreateAPIView,
    StudentDetailAPIView,
    EnrollmentListCreateAPIView,
    EnrollmentDetailAPIView,
)
urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<str:admission_number>/', StudentDetailAPIView.as_view(), name='student-detail'),

    path('enrollments/', EnrollmentListCreateAPIView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentDetailAPIView.as_view(), name='enrollment-detail'),
]