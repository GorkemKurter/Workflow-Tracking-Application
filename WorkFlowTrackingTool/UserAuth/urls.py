from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'UserAuth'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('main_page/',views.main,name="main"),
    path('component_requests/', views.component_requests, name='component_requests'),
    path('component_requests/edit/<int:id>/', views.edit_component_request, name='edit_component_request'),
    path('component_requests/add/', views.add_component_request, name='add_component_request'),
    path('component_requests/delete/<int:id>/', views.delete_component_request, name='delete_component_request'),
    path('component/', views.component, name='component'),
    path('component/edit/<int:id>/', views.edit_component, name='edit_component'),
    path('component/add/', views.add_component, name='add_component'),
    path('component/delete/<int:id>/', views.delete_component, name='delete_component'),
    path('component/forbidden', views.forbidden, name='forbidden'),
    path('component_requests/export_to_csv', views.cpRequest_export_csv, name='cpRequest_export_csv'),
    path('component/export_to_csv', views.cp_export_csv, name='cp_export_csv'),
    path('account/',views.account, name='accounts'),
    path('account/add_account',views.add_account, name='add_accounts'),
    path('account/edit_account/<int:id>/',views.edit_account, name='edit_accounts'),
    path('account/delete_account/<int:id>/',views.delete_account, name='delete_accounts'),
    path('account/download/<int:id>/', views.download_order, name='download_order'),
    path('media/standards/<str:filename>/', views.serve_file, name='serve_file'),
    path('EMC/', views.EMC_table, name='EMC_table'),
    path('EMC/add', views.add_EMC, name='add_EMC'),
    path('EMC/edit/<int:id>/', views.edit_EMC, name='edit_EMC'),
    path('EMC/delete/<int:id>/', views.delete_EMC, name='delete_EMC'),
    path('EMC/download/<int:id>/', views.download_EUT_Description, name='download_EUT_Description')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)