from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('room/<int:room_id>/', views.room_detail, name='room'),
    path('report/', views.inspection_report, name='report'),
]