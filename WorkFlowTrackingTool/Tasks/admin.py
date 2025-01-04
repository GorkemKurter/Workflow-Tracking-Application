from django.contrib import admin
from .models import Task, SubTask, Account, EMC, E_lab
from .forms import TaskCreationForm, TaskUpdateForm, E_labAdminForm
# Register your models here.

class SubtaskInLine(admin.TabularInline):
    model = SubTask
    extra = 1
    max_num = 5

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form =TaskUpdateForm
    add_form =  TaskCreationForm
    list_display = ["Task_title","Task_Priority","Task_status","Task_Created_at","Task_Updated_at","Task_Due_Date"]
    inlines = [SubtaskInLine]
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs['form'] = self.add_form
        else:
            kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account

@admin.register(EMC)
class EMCAdmin(admin.ModelAdmin):
    model = EMC

@admin.register(E_lab)
class E_labAdmin(admin.ModelAdmin):
    model = E_lab
    form = E_labAdminForm