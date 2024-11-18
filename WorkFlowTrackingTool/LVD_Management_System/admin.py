from django.contrib import admin
from .models import Component, Component_Request
from .forms import Component_RequestAdminForm
# Register your models here.

admin.site.site_title = "Test Management System"
admin.site.site_header = "VESTEL IECEE Test Management"
admin.site.index_title = "IECEE Test Magement" 

class ComponentAdmin(admin.ModelAdmin):
    search_fields = ['Part_name','Manufacturer','Model','Standard','SAP_code']
    list_display = ['Part_name','Manufacturer','Model','SAP_code','T_Washer_LVD','F_Washer_LVD','T_Washer_Dryer_LVD',
                    'F_Washer_Dryer_LVD','N_Washer_LVD']
    list_filter = ['T_Washer_LVD','F_Washer_LVD',
                     'T_Washer_Dryer_LVD','F_Washer_Dryer_LVD','N_Washer_LVD']
    
class Component_RequestAdmin(admin.ModelAdmin):
    search_fields = ['R_Part_name','R_Manufacturer','R_Model','R_Standard','R_SAP_code']
    list_display = ['R_Part_name','R_Manufacturer','R_Model','R_SAP_code','R_T_Washer_LVD','R_F_Washer_LVD','R_T_Washer_Dryer_LVD',
                    'R_F_Washer_Dryer_LVD','R_N_Washer_LVD']
    list_filter = ['R_T_Washer_LVD','R_F_Washer_LVD',
                     'R_T_Washer_Dryer_LVD','R_F_Washer_Dryer_LVD','R_N_Washer_LVD']
    
    form = Component_RequestAdminForm
    

admin.site.register(Component,ComponentAdmin)
admin.site.register(Component_Request, Component_RequestAdmin)
