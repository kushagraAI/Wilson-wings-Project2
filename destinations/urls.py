from django.urls import path
from . import views
from rest_framework import renderers
from destinations.views import DestinationViewSet, UserViewSet

urlpatterns = [

    path('users/', views.UserViewSet.as_view({
        'get': 'list'}), name='user-list'),
    path('users/<int:pk>/', views.UserViewSet.as_view({
        'get': 'retrieve'}), name='user-detail'),
    path('destinations/', views.DestinationViewSet.as_view({
        'get': 'list',
        'post': 'create'}), name='destination-list'),
    path('destinations/<int:pk>/', views.DestinationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'}), name='destination-detail'),

]
