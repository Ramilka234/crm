from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('users/', views.ListUsers.as_view()),
    path('houses/', views.HousesViewSet.as_view({'get': 'list'})),
    path('houses/<int:pk>/', views.HousesViewSet.as_view({'get': 'retrieve'})),
])