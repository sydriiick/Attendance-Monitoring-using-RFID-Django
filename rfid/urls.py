from django.urls import path
from . import views

urlpatterns = [
    path('attendance-list', views.attendanceList, name='attendance-list'),
    path('attendance-detail/<str:pk>', views.attendanceDetail, name='attendance-detail'),
    path('attendance-create', views.attendanceCreate, name='attendance-create'),
    path('attendance-update', views.attendanceUpdate, name='attendance-update'),
    
]