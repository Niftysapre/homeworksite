from django.urls import path
from . import views
from .views import download_file

urlpatterns = [
    path('', views.notify, name='main'),
    path('notify/', views.notify, name='notify'),
    path('lessons/', views.lessons, name='lessons'),
    path('classes/', views.classes, name='classes'),
    path('checking/', views.checkin, name='checking'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]
