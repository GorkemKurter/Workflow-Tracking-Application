from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from .utils import order_upload_to, emc_upload_to, e_lab_upload_to


class Task(models.Model):
    Task_title = models.CharField(max_length=100,verbose_name="Görev Başlığı")
    Task_Description = models.TextField(verbose_name="Görev İçeriği")
    Task_Status_Choices = [("NotResolved","Tamamlanmadı"),("Ongoing","Devam Ediyor"),("Finished","Tamamlandı"),("Pending","Beklemede"),("Cancelled","İptal Edildi")]
    Task_status = models.CharField(max_length=20,verbose_name="Son Durum",choices=Task_Status_Choices,default="NotResolved")
    Task_Created_at = models.DateField(auto_now_add=True,verbose_name="Görevin atandığı zaman")
    Task_Updated_at = models.DateField(auto_now=True,verbose_name="Son güncelleme")
    Task_Asigned_at = models.ManyToManyField(Group,verbose_name="Görev Atanan Grup")
    Task_Due_Date = models.DateField(null=True,blank=True,verbose_name="Termin Tarihi")
    Task_Priority_Choices = [("High","Yüksek"),("Normal","Normal"),("Low","Düşük")]
    Task_Priority = models.CharField(max_length=10,choices=Task_Priority_Choices,verbose_name="Öncelik Düzeyi",default=Task_Priority_Choices[1][1])
    def __str__(self):
        return self.Task_title
    
class SubTask(models.Model):
    Subtask_title = models.CharField(max_length=100, verbose_name="Alt Görev Başlığı")
    Subtask_Description = models.TextField(verbose_name="Alt Görev İçeriği")
    Subtask_status_choices = [("NotResolved","Tamamlanmadı"),("Ongoing","Devam Ediyor"),("Finished","Tamamlandı"),("Pending","Beklemede"),("Cancelled","İptal Edildi")]
    Subtask_status = models.CharField(max_length=20, verbose_name="Durum", choices=Subtask_status_choices, default="NotResolved")
    Subtask_due_date = models.DateField(null=True, blank=True, verbose_name="Termin Tarihi")
    Subtask_Priority_Choices = [("High","Yüksek"),("Normal","Normal"),("Low","Düşük")]
    Subtask_Priority = models.CharField(max_length=10,choices=Subtask_Priority_Choices,verbose_name="Öncelik Düzeyi",default="Normal")
    Parent_task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name="subtasks", verbose_name="Ana Görev")
    Subtask_Asigned_at = models.ManyToManyField(User,verbose_name="Görev Atanan")
    Subtask_Created_at = models.DateField(auto_now_add=True,verbose_name="Görevin atandığı zaman")
    Subtask_Updated_at = models.DateField(auto_now=True,verbose_name="Son güncelleme")
    
    def clean(self):
        if self.parent_task.subtasks.count() >= 3:
            raise ValidationError('Bu görev en fazla 3 alt görev içerebilir.')
        
    def __str__(self):
        return self.Subtask_title

class Account(models.Model):
    Topic = models.CharField(max_length=100, verbose_name="Konu")
    Company = models.CharField(max_length=100, verbose_name="Firma")
    Month = models.DateField(auto_now_add=True,verbose_name="Tarih")
    Year = models.CharField(max_length=100, verbose_name="Yıl")
    Requester = models.ForeignKey("auth.User",on_delete = models.PROTECT,default = 1,verbose_name='Talep Eden')
    SAT = models.CharField(max_length=100, verbose_name="SAT No.")
    SAS = models.CharField(max_length=100, verbose_name="SAS No.")
    Amount = models.CharField(max_length=100, verbose_name="Tutar")
    Currency = models.CharField(max_length=100, verbose_name="Para Birimi")
    Status = models.CharField(max_length=100, verbose_name="Onay Durumu")
    Comments = models.CharField(max_length=200, verbose_name="Açıklama")
    Order = models.FileField(upload_to=order_upload_to, verbose_name="Teklif", null=True, blank=True)
    
    def formatted_month(self):
        return self.Month.strftime('%d.%m.%y')
    
    def __str__(self):
        return self.Topic
    
class E_lab(models.Model):
    
    Requester = models.ForeignKey("auth.User",on_delete = models.PROTECT,default = 1,verbose_name='Talep Eden',related_name='e_lab_Requester')
    Requested_to = models.ManyToManyField(User,verbose_name='Atanan',related_name='e_lab_Requested_to')
    Date = models.DateTimeField(auto_now_add=True,verbose_name="Tarih")
    Last_Update = models.DateTimeField(auto_now=True,verbose_name="Son Güncelleme")
    Topic = models.CharField(max_length=100, verbose_name="Konu")
    Content = models.TextField(verbose_name="İçerik")
    Status = models.CharField(max_length=100, verbose_name="Görev Durumu")
    Test_Files = models.FileField(upload_to=e_lab_upload_to, verbose_name="Test Dosyaları", null=True, blank=True)
    Status_Choices = [("NotResolved","Tamamlanmadı"),("Ongoing","Devam Ediyor"),("Finished","Tamamlandı"),("Pending","Beklemede"),("Cancelled","İptal Edildi")]
    Priority_Choices = [("High","Yüksek"),("Normal","Normal"),("Low","Düşük")]
    Priority = models.CharField(max_length=100, verbose_name="Öncelik",choices=Priority_Choices,default="Normal")
    Status = models.CharField(max_length=100, verbose_name="Durum",choices=Status_Choices,default="NotResolved")

    def formatted_date(self):
        return self.Date.strftime('%d.%m.%y')
    
    def formatted_last_update(self):
        return self.Last_Update.strftime('%d.%m.%y')

    def __str__(self):
        return self.Topic

class EMC(models.Model):
    Requester = models.ForeignKey("auth.User",on_delete = models.PROTECT,default = 1,verbose_name='Talep Eden',related_name='emc_Requester')
    Topic = models.CharField(max_length=100,verbose_name="Test")
    Notes = models.TextField(verbose_name="Notlar",blank=True,null=True)
    Number = models.CharField(max_length=100,verbose_name="Test Numarası")
    Machine = models.CharField(max_length=100,verbose_name="Test Makinesi")
    EUT_Description = models.FileField(upload_to=emc_upload_to,verbose_name="EUT File",null=True,blank=True)
    Delivery_Date = models.DateField(verbose_name="Teslim Tarihi",auto_now_add=True)
    Update_Date = models.DateField(auto_now=True,verbose_name="Son Güncelleme")
    Status_Chocies = [("NotResolved","Tamamlanmadı"),("Ongoing","Devam Ediyor"),("Finished","Tamamlandı"),("Pending","Beklemede"),("Cancelled","İptal Edildi")]
    Status = models.CharField(max_length=100,verbose_name="Durum",choices=Status_Chocies,default="NotResolved")
    Result_Choices = [("Pass","Geçti"),("Fail","Başarısız"),("Ongoing","Devam Ediyor")]
    Test_link = models.CharField(verbose_name="Test Linki",blank=True,null=True,max_length=200)
    Result = models.CharField(max_length=100,verbose_name="Sonuç",choices=Result_Choices)


    def formatted_delivery_date(self):
        return self.Delivery_Date.strftime('%d.%m.%y')
    
    def formatted_update_date(self):
        return self.Update_Date.strftime('%d.%m.%y')

    def __str__(self):
        return self.Topic

class EMC_Test(models.Model):

    EMC = models.ForeignKey(to=EMC,on_delete = models.CASCADE,verbose_name="EMC Testi")
    Conducted_Emission = models.CharField(max_length=100,verbose_name="Conducted Emission",null=True,blank=True)
    Flicker = models.CharField(max_length=100,verbose_name="Flicker",null=True,blank=True)
    Discharge = models.CharField(max_length=100,verbose_name="Electrostatic Discharge",null=True,blank=True)
    Harmonic = models.CharField(max_length=100,verbose_name="Harmonic",null=True,blank=True)
    Burst = models.CharField(max_length=100,verbose_name="Burst",null=True,blank=True)
    Surge = models.CharField(max_length=100,verbose_name="Surge",null=True,blank=True)
    Conducted_Disturbance = models.CharField(max_length=100,verbose_name="Conducted Disturbance",null=True,blank=True)
    Voltage_Dips = models.CharField(max_length=100,verbose_name="Voltage Dips",null=True,blank=True)
    Disturbance_Power = models.CharField(max_length=100,verbose_name="Disturbance Power",null=True,blank=True)
    Radiated_Impunity = models.CharField(max_length=100,verbose_name="Radiated Immunity",null=True,blank=True)
    Discontinious_Disturbance = models.CharField(max_length=100,verbose_name="Discontinious Disturbance",null=True,blank=True)

class EUT_Hardware(models.Model):

    EMC = models.ForeignKey(to=EMC,on_delete = models.CASCADE,verbose_name="EMC Testi")
    Pump = models.CharField(max_length=100,verbose_name="Pump",null=True,blank=True)
    Motor = models.CharField(max_length=100,verbose_name="Motor",null=True,blank=True)
    Fan = models.CharField(max_length=100,verbose_name="Fan",null=True,blank=True)
    EMI_Filter = models.CharField(max_length=100,verbose_name="EMI Filter",null=True,blank=True)
    Main_Board = models.CharField(max_length=100,verbose_name="Main Board",null=True,blank=True)
    Display = models.CharField(max_length=100,verbose_name="Display",null=True,blank=True)
    Driver_Board = models.CharField(max_length=100,verbose_name="Driver Board",null=True,blank=True)
    Twinjet = models.BooleanField(verbose_name="Twinjet",null=True,blank=True)
    Circulation_Pump = models.CharField(max_length=100,verbose_name="Circulation Pump",null=True,blank=True)

class EUT_Software(models.Model):

    EMC = models.ForeignKey(to=EMC,on_delete = models.CASCADE,verbose_name="EMC Testi")
    Main_Board_Software = models.CharField(max_length=100,verbose_name="Main Board Software",null=True,blank=True)
    Display_Software = models.CharField(max_length=100,verbose_name="Display Software",null=True,blank=True)
    Driver_Board_Software = models.CharField(max_length=100,verbose_name="Driver Board Software",null=True,blank=True)
    MPF = models.CharField(max_length=100,verbose_name="MPF",null=True,blank=True)