from django import forms
from django.forms import inlineformset_factory
from .models import Task, Account, E_lab, EMC, EMC_Test ,EUT_Hardware, EUT_Software
from django.urls import reverse

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

class AccountAdminForm(forms.ModelForm):
    remove_order = forms.BooleanField(required=False, label='Remove current invoice')

    class Meta:
        model = Account
        widgets = {
            'Order': forms.FileInput(),
        }
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(AccountAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.Order:
                self.download_url = reverse('UserAuth:download_order', args=[self.instance.pk])
    
    def save(self, commit=True):
        account = super(AccountAdminForm, self).save(commit=False)
        if self.cleaned_data.get('remove_order'):
            account.Order.delete()
            account.Order = None
        if commit:
            account.save()
        return account

class E_labAdminForm(forms.ModelForm):
    remove_Test_Files = forms.BooleanField(required=False, label='Mevcut test dosyasını kaldır')

    class Meta :
        model = E_lab
        widgets = {
            'Test_Files': forms.FileInput(),
        }
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(E_labAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.Test_Files:
                self.download_url = reverse('UserAuth:download_Test_File', args=[self.instance.pk])
                
    def save(self, commit=True):
        Record = super(E_labAdminForm, self).save(commit=False)
        if self.cleaned_data.get('remove_Test_Files'):
            Record.Test_Files.delete()
            Record.Test_Files = None
        if commit:
            Record.save()
        return Record


class EMCAdminForm(forms.ModelForm):
    

    class Meta :
        model = EMC
        widgets = {
            'EUT_Description': forms.FileInput(),
        }
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(EMCAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.EUT_Description:
                self.download_url = reverse('UserAuth:download_EUT_Description', args=[self.instance.pk])

    remove_EUT_Files = forms.BooleanField(required=False, label='Remove current EUT Description')
    
    def save(self, commit=True):
        Record = super(EMCAdminForm, self).save(commit=False)
        if self.cleaned_data.get('remove_EUT_Files'):
            Record.EUT_Description.delete()
            Record.EUT_Description = None
        if commit:
            Record.save()
        return Record

class EMC_TestAdminForm(forms.ModelForm):

    class Meta :
        model = EMC_Test
        fields = '__all__'


EMCTestFormSet = inlineformset_factory(
    EMC, 
    EMC_Test,
    fields=('Conducted_Emission', 'Flicker', 'Discharge', 'Harmonic', 
            'Burst', 'Surge', 'Conducted_Disturbance', 'Voltage_Dips',
            'Disturbance_Power', 'Radiated_Impunity', 'Discontinious_Disturbance'),
    extra=0,
    can_delete=False
)

EMCHardwareFormSet = inlineformset_factory(
    EMC,
    EUT_Hardware,
    fields=('Pump', 'Motor', 'Fan', 'EMI_Filter', 'Main_Board', 'Display', 'Driver_Board', 'Twinjet', 'Circulation_Pump'),
    extra=0,
    can_delete=False
)

EMCSoftwareFormSet = inlineformset_factory(
    EMC,
    EUT_Software,
    fields=('Main_Board_Software', 'Display_Software', 'Driver_Board_Software', 'MPF'),
    extra=0,
    can_delete=False
)