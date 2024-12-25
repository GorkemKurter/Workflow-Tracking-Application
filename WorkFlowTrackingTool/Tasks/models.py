from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from datetime import datetime
import os
from django.utils.text import slugify


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

class IECEE_tests(models.Model):
    Title = models.CharField(max_length=100, verbose_name="Test Konusu")
    EUT_component = models.CharField(max_length=100, verbose_name="Test Edilecek Komponent/Parça/Makine")
    Test_type_choices = [('Malzeme','Malzeme'),('Elektriksel','Elektriksel')]
    Test_type = models.CharField(verbose_name="Test Türü",max_length=30,choices=Test_type_choices)
    Description = models.TextField(verbose_name="Açıklama")
    Test_result_choices = [('OK','OK'),('NOK','NOK'),('Kararsız','Kararsız')]
    Test_result = models.CharField(verbose_name="Test Sonucu",max_length=30,choices=Test_result_choices)
    Test_link = models.CharField(max_length=300,verbose_name='Test Linki',help_text='Test dosyalarının bulunduğu klasör linki')
    Comments = models.TextField(verbose_name="Gözlemler/Yorumlar")
    Test_create_date = models.DateField(auto_now_add=True)
    Test_update_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.Title

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
    Order = models.FileField(upload_to='orders/', verbose_name="Teklif")
    
    def formatted_month(self):
        return self.Month.strftime('%d.%m.%y')
    
    def __str__(self):
        return self.Topic
