from django.urls import path
from . import views
app_name = 'UserAuth'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('main_page/',views.main,name="main"),
    path('component_requests/', views.component_requests, name='component_requests'),
    path('component_requests/edit/<int:id>/', views.edit_component_request, name='edit_component_request'),
    path('component_requests/add/', views.add_component_request, name='add_component_request'),
]
