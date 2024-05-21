from django.urls import path
from .views import StudentList, StudentDetail, BuildingList, BuildingDetail, ApartmentList, ApartmentDetail, RoomList, RoomDetail, StudentAssignment

urlpatterns = [
    # CRUDS
    path('student/', StudentList.as_view(), name="student-list"),
    path('student/<str:pk>/', StudentDetail.as_view(), name="student-detail"),
    path('building/', BuildingList.as_view(), name='building-list'),
    path('building/<int:pk>', BuildingDetail.as_view(), name='building-detail'),
    path('apartment/', ApartmentList.as_view(), name='apartment-list'),
    path('apartment/<int:pk>', ApartmentDetail.as_view(), name='apartment-detail'),
    path('room/', RoomList.as_view(), name='room-list'),
    path('room/<int:pk>', RoomDetail.as_view(), name='room-detail'),

    # Use Cases
    path('student-asignment/', StudentAssignment.as_view(), name='student-asignment'),
]