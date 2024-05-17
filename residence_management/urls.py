from django.urls import path
from.views import ApartmentDetailView, ApartmentListView, CreateUserView

urlpatterns = [
    path('apartments/', ApartmentListView.as_view(), name='apartment-list'),
    path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    path('register', CreateUserView.as_view(), name='register')
]