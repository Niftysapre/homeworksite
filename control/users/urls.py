from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.registerUser.as_view(), name='register'), 
    path('profile/', views.ProfileUser.as_view(), name='profile'),
]
