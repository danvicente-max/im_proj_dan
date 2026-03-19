from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('room/<int:room_id>/', views.room_detail, name='room'),
    path('laboratory/', views.laboratory, name='laboratory'),
    path('inspection/', views.inspection_form, name='inspection_form'),
    path('report/', views.report, name='report'),
    
    path("add-lab/", views.add_lab, name="add_lab"),
    path("delete-lab/<int:room_id>/", views.delete_lab, name="delete_lab"),

    path("add-unit/", views.add_unit, name="add_unit"),
    path("delete-unit/<int:unit_id>/", views.delete_unit, name="delete_unit"),
]