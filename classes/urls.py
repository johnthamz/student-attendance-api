from django.urls import path
from .views import ClassroomListCreateAPIView, ClassroomDetailAPIView

urlpatterns = [
    path('classrooms/', ClassroomListCreateAPIView.as_view(), name='classroom-list-create'),
    path(
        'classrooms/<int:pk>/',
        ClassroomDetailAPIView.as_view(),
        name='classroom-detail'
    ),
]

