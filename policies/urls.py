from django.urls import path
from . import views

urlpatterns = [
    path('summary/<str:batch_id>/', views.summary_report, name='summary_report'),
    path('detail/', views.detail_report, name='detail_report'),
    path('', views.dashboard, name='dashboard'),
    path('', views.home, name="home")
]