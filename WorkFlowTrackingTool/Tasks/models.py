from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError

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
    Subtask_status_choices = [("NotResolved", "Tamamlanmadı"), ("Ongoing", "Devam Ediyor"), ("Finished", "Tamamlandı")]
    Subtask_status = models.CharField(max_length=20, verbose_name="Durum", choices=Subtask_status_choices, default="NotResolved")
    Subtask_due_date = models.DateField(null=True, blank=True, verbose_name="Termin Tarihi")
    Subtask_Priority_Choices = [("High","Yüksek"),("Normal","Normal"),("Low","Düşük")]
    Subtask_Priority = models.CharField(max_length=10,choices=Subtask_Priority_Choices,verbose_name="Öncelik Düzeyi",default="Normal")
    Parent_task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name="subtasks", verbose_name="Ana Görev")
    Subtask_Asigned_at = models.ManyToManyField(User,verbose_name="Görev Atanan")
    Subtask_Created_at = models.DateField(auto_now_add=True,verbose_name="Görevin atandığı zaman")
    Subtask_Updated_at = models.DateField(auto_now=True,verbose_name="Son güncelleme")
    
    def clean(self):
        if self.parent_task.subtasks.count() >= 5:
            raise ValidationError('Bu görev en fazla 3 alt görev içerebilir.')
        
    def __str__(self):
        return self.Subtask_title