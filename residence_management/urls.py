from django.urls import path
from .views import StudentList, StudentDetail

urlpatterns = [
    path('students/', StudentList.as_view(), name="student-list"),
    path('students/<str:pk>/', StudentDetail.as_view(), name="student-detail"),
    # path('apartments/', ApartmentListView.as_view(), name='apartment-list'),
    # path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    # path('register', CreateUserView.as_view(), name='register')
]