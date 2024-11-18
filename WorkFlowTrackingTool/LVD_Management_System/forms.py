from django import forms
from .models import Component_Request
from django.utils.html import format_html

class Component_RequestAdminForm(forms.ModelForm):
    
    class Meta :
        model = Component_Request
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(Component_RequestAdminForm, self).__init__(*args, **kwargs)
        self.fields['R_Part_name'].help_text = format_html(
            '<a href="/static/Test-Requirements.pdf"download>Download Guidebook</a>'
        )