from django.urls import path
from . import views

app_name = 'configPC'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pc_id>/', views.detail, name = 'detail'),
    path('leave_pc/', views.leave_pc, name = 'leave_pc'),
]
