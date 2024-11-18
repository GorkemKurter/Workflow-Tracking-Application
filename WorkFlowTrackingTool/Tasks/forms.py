from django import forms
from .models import Task

class TaskCreationForm(forms.ModelForm):
    
    class Meta:
        form = Task
        model = Task
        exclude = ["Task_status","Task_Updated_at","Task_Created_at"]
    
        
class TaskUpdateForm(forms.ModelForm):
    
    class Meta:
        form = Task
        model = Task
        fields = ["Task_Description","Task_status","Task_Asigned_at","Task_Due_Date","Task_Priority"]