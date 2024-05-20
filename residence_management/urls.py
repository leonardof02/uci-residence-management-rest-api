from django.urls import path
from .views import StudentList, StudentDetail, BuildingList, BuildingDetail

urlpatterns = [
    path('students/', StudentList.as_view(), name="student-list"),
    path('students/<str:pk>/', StudentDetail.as_view(), name="student-detail"),
    path('building/', BuildingList.as_view(), name='building-list'),
    path('building/<int:pk>', BuildingDetail.as_view(), name='building-detail'),
]