from django.urls import path
from . import views

app_name = 'LVD_Management_System'

urlpatterns = [
    path('component_requests/', views.component_requests, name='component_requests')
]