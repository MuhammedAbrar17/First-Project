# admindashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('userdetails/', views.user_details, name = 'userdetails'),
    path('useraction/<int:id>', views.user_action, name = 'useraction'),
    path('search_users/', views.search_users, name = 'searchusers'),
]