from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login as alogin,authenticate,logout as dlogout
from django.contrib.auth.decorators import login_required
from LVD_Management_System.models import Component_Request,Component
from LVD_Management_System.forms import Component_RequestAdminForm, ComponentAdminForm
from Tasks.forms import AccountAdminForm, EMCAdminForm, EMCTestFormSet, EMCHardwareFormSet, EMCSoftwareFormSet, E_labAdminForm
from Tasks.models import Account, EMC, E_lab
import pandas as pd
from django.http import HttpResponse, HttpResponseNotFound
from .utils import auto_mail_sender
from django.http import FileResponse
import os

#Register/Login Part

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            e_mail = form.cleaned_data.get('e_mail')
            password = form.cleaned_data.get('password')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return render(request, 'register.html', {'form': form})
            if User.objects.filter(email=e_mail).exists():
                messages.error(request, 'Email is already registered.')
                return render(request, 'register.html', {'form': form})
            user = User.objects.create_user(username=username, email=e_mail, password=password)
            user.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('UserAuth:login')
        return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request,'Username or password is wrong!')
            pass
        else:
            alogin(request, user)
            return redirect('UserAuth:main')
        return render(request,'login.html',{'form':form})
    else:
        form = LoginForm()
    
    return render(request,'login.html',{'form':form})

def logout(request): 
    
    dlogout(request) 
    return redirect('UserAuth:login')

@login_required(login_url='UserAuth:login')
def main(request):
    
    return render(request,'main_page.html')

#Component Request Part

@login_required(login_url='UserAuth:login')
def component_requests(request):
    sort_by = request.GET.get('sort_by', 'R_Last_Update_Date')
    order = request.GET.get('order', 'desc')
    if order == 'asc':
        component_requests = Component_Request.objects.all().order_by(sort_by)
    else:
        component_requests = Component_Request.objects.all().order_by(f'-{sort_by}')
    context = {
        'component_requests' : component_requests,
        'current_order' : order,
        'current_sort_by': sort_by
    }
    return render(request, 'component_requests.html', context)

@login_required(login_url='UserAuth:login')
def edit_component_request(request, id):
    component_request = get_object_or_404(Component_Request, id=id)
    current_username = component_request.R_Requester
    user = User.objects.get(username=current_username)
    user_mail = user.email
    admin_emails = list(User.objects.filter(is_superuser=True).values_list('email', flat=True))
    if request.user != component_request.R_Requester and not request.user.is_superuser:
        form = Component_RequestAdminForm(instance=component_request)
        return render(request, 'view_component_request.html', {'form': form})
    
    if request.method == 'POST':
        form = Component_RequestAdminForm(request.POST, instance=component_request)
        if form.is_valid():
            component_request = form.save(commit=False)
            if component_request.R_Status == "Approved":
                save_component_from_request(component_request)
                auto_mail_sender(subject="!!!VESTEL IECEE Test Management Automatic E-mail!!!",content=f'''Dear Requester,\nYour component request is approved and it will be added to relevant CB test reports. {request.user.username}.
    Part Name : {form.cleaned_data.get('R_Part_name')},
    Manufacturer Name : {form.cleaned_data.get('R_Manufacturer')},
    Model Name : {form.cleaned_data.get('R_Model')},
    Explanation of component/Deleted Because : {form.cleaned_data.get('R_Determination')}\nBest Regards''',to=admin_emails + [user_mail])
                component_request.save()
            else:
                auto_mail_sender(subject="!!!VESTEL IECEE Test Management Automatic E-mail!!!",content=f'''Dear Requester,\nYour component request is modified by {request.user.username}.
    Part Name : {form.cleaned_data.get('R_Part_name')},
    Manufacturer Name : {form.cleaned_data.get('R_Manufacturer')},
    Model Name : {form.cleaned_data.get('R_Model')},
    Explanation of component/Deleted Because : {form.cleaned_data.get('R_Determination')}\nBest Regards''',to=admin_emails + [user_mail])
                component_request.save()
            return redirect('UserAuth:component_requests')
    else:
        form = Component_RequestAdminForm(instance=component_request)
    return render(request, 'edit_component_request.html', {'form': form, 'editable': True})

@login_required(login_url='UserAuth:login')
def add_component_request(request):
    if request.method == 'POST':
        form = Component_RequestAdminForm(request.POST)
        if form.is_valid():
            component_request = form.save(commit=False)
            component_request.R_Requester = request.user
            component_request.R_Status = 'Pending'
            component_request.save()
            return redirect('UserAuth:component_requests')
    else:
        form = Component_RequestAdminForm(initial={'R_Requester': request.user, 'R_Status': "Pending"})
    return render(request, 'add_component_request.html', {'form': form})

@login_required(login_url='UserAuth:login')
def delete_component_request(request, id):
    component_request = get_object_or_404(Component_Request, id=id)
    current_username = component_request.R_Requester
    user = User.objects.get(username=current_username)
    old_determination = component_request.R_Determination
    user_email = user.email
    if request.method == 'POST':
        determination = request.POST.get('determination', old_determination)
        component_request.delete()
        auto_mail_sender(subject='!!!VESTEL IECEE Test Management Automatic E-mail!!!',content=f'''Dear Sender,
                        Your component is deleted by {request.user.username}.\n
    Part Name : {component_request.R_Part_name},
    Manufacturer Name : {component_request.R_Manufacturer},
    Model Name : {component_request.R_Model},
    Explanation of component/Deleted Because : {determination}\nBest Regards''',to=[user_email])
        return redirect('UserAuth:component_requests')
    return render(request, 'edit_component_request.html', {'form': Component_RequestAdminForm(instance=component_request)})

#LVD Components Part
@login_required(login_url='UserAuth:login')
def component(request):
    sort_by = request.GET.get('sort_by', 'Last_Update_Date')
    order = request.GET.get('order', 'desc')
    if order == 'asc':
        components = Component.objects.all().order_by(sort_by)
    else:
        components = Component.objects.all().order_by(f'-{sort_by}')
    context = {
        'components': components,
        'current_order': order
    }
    return render(request,'components.html',context)

@login_required(login_url='UserAuth:login')
def edit_component(request, id):
    component = get_object_or_404(Component, id=id)
    if not request.user.is_superuser:
        form = ComponentAdminForm(instance=component)
        return render(request, 'view_components.html',{'form':form,})
    if request.method == 'POST':
        form = ComponentAdminForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            return redirect('UserAuth:component')
    else:
        form = ComponentAdminForm(instance=component)
    return render (request, 'edit_components.html', {'form': form, 'editable': True})
        
        
@login_required(login_url='UserAuth:login')
def add_component(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ComponentAdminForm(request.POST)
            if form.is_valid():
                component = form.save(commit=False)
                component.save()
                return redirect('UserAuth:component')
        else:
            form = ComponentAdminForm()
        return render(request, 'add_components.html', {'form': form})
    else:
        return redirect('UserAuth:forbidden')

@login_required(login_url='UserAuth:login')
def delete_component(request, id):
    component = get_object_or_404(Component, id=id)
    if request.method == 'POST':
        component.delete()
        return redirect('UserAuth:component')
    return render(request, 'components.html', {'form': ComponentAdminForm(instance=component)})

@login_required(login_url='UserAuth:login')
def forbidden(request):
    return render(request, 'forbidden.html')

def save_component_from_request(request):
    Component.objects.create(
        Part_name=request.R_Part_name,
        Manufacturer=request.R_Manufacturer,
        Model=request.R_Model,
        Technical_Data=request.R_Technical_Data,
        Standard='-',
        Mark_of_Conformity='-',
        T_Washer_LVD=request.R_T_Washer_LVD,
        T_Washer_Dryer_LVD=request.R_T_Washer_Dryer_LVD,
        F_Washer_LVD=request.R_F_Washer_LVD,
        F_Washer_Dryer_LVD=request.R_F_Washer_Dryer_LVD,
        N_Washer_LVD=request.R_N_Washer_LVD,
        SAP_code=request.R_SAP_code,
        Certificate_Expiry_Date='1999-11-11',
        Test_Results_Link=request.Test_Results_Link,
    )

@login_required(login_url='UserAuth:login')
def cpRequest_export_csv(request):
    component_requests = Component_Request.objects.all().values()
    df = pd.DataFrame(component_requests)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=component_requests.xlsx'
    df.to_excel(response, index=False)
    return response

@login_required(login_url='UserAuth:login')
def cp_export_csv(request):
    component = Component.objects.all().values()
    df = pd.DataFrame(component)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=LVD_components.xlsx'
    df.to_excel(response, index=False)
    return response

#Account Part
@login_required(login_url='UserAuth:login')
def account(request):
    sort_by = request.GET.get('sort_by', 'id')
    order = request.GET.get('order', 'desc')
    if order == 'asc':
        accounts = Account.objects.all().order_by(sort_by)
    else:
        accounts = Account.objects.all().order_by(f'-{sort_by}')
    context = {
        'accounts': accounts,
        'current_order': order
    }
    return render(request,'accounts.html',context)

@login_required(login_url='UserAuth:login')
def add_account(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AccountAdminForm(request.POST,request.FILES)
            if form.is_valid():
                component = form.save(commit=False)
                component.save()
                return redirect('UserAuth:accounts')
        else:
            form = AccountAdminForm()
        return render(request, 'add_accounts.html', {'form': form})
    else:
        return redirect('UserAuth:forbidden')
    
@login_required(login_url='UserAuth:login')
def edit_account(request, id):
    account = get_object_or_404(Account, id=id)
    if not request.user.is_superuser:
        return render(request, 'accounts.html')
    if request.method == 'POST':
        form = AccountAdminForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('UserAuth:accounts')
    else:
        form = AccountAdminForm(instance=account)
    return render (request, 'edit_accounts.html', {'form': form, 'editable': True})

@login_required(login_url='UserAuth:login')
def delete_account(request, id):
    account = get_object_or_404(Account, id=id)
    if request.method == 'POST':
        account.delete()
        return redirect('UserAuth:accounts')
    return render(request, 'accounts.html', {'form': ComponentAdminForm(instance=account)})

@login_required(login_url='UserAuth:login')
def download_order(request, id):
    account = get_object_or_404(Account, id=id)
    if os.path.exists(account.Order.path):
        response = FileResponse(account.Order.open(), as_attachment=True, filename=account.Order.name.split('/')[-1])
        return response
    else:
        return HttpResponseNotFound('File not found')

#Standards Part

@login_required(login_url='UserAuth:login')
def serve_file(request, filename):
    file_path = os.path.join('media/standards', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
        return HttpResponseNotFound('File not found')
    
#EMC Part

@login_required(login_url='UserAuth:login')
def EMC_table(request):
    sort_by = request.GET.get('sort_by', 'Update_Date')
    order = request.GET.get('order', 'desc')
    if order == 'asc':
        EMC_datas = EMC.objects.all().order_by(sort_by)
    else:
        EMC_datas = EMC.objects.all().order_by(f'-{sort_by}')
    context = {
        'EMC_datas': EMC_datas,
        'current_order': order
    }
    return render(request,'EMC_records.html', context=context)

@login_required(login_url='UserAuth:login')
def add_EMC(request):
    if request.method == 'POST':
        form = EMCAdminForm(request.POST, request.FILES)
        formset = EMCTestFormSet(request.POST)
        formset_hardware = EMCHardwareFormSet(request.POST)
        formset_software = EMCSoftwareFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            emc = form.save()
            formset.instance = emc
            formset_hardware.instance = emc
            formset_software.instance = emc
            formset.save()
            formset_hardware.save()
            formset_software.save()
            return redirect('UserAuth:EMC_table')
    else:
        form = EMCAdminForm()
        formset = EMCTestFormSet()
        formset_hardware = EMCHardwareFormSet()
        formset_software = EMCSoftwareFormSet()
    return render(request, 'add_EMC.html', {
        'form': form,
        'formset': formset,
        'formset_hardware': formset_hardware,
        'formset_software': formset_software
    })

@login_required(login_url='UserAuth:login')
def edit_EMC(request, id):
    EMC_record = get_object_or_404(EMC, id=id)
    if not request.user.is_superuser:
        form = EMCAdminForm(instance=EMC_record)
        formset = EMCTestFormSet(instance=EMC_record)
        formset_hardware = EMCHardwareFormSet(instance=EMC_record)
        formset_software = EMCSoftwareFormSet(instance=EMC_record)
        return render(request, 'view_EMC.html', {'form': form, 
                                                 'formset': formset, 
                                                 'formset_hardware': formset_hardware, 
                                                 'formset_software': formset_software})
    if request.method == 'POST':
        form = EMCAdminForm(request.POST, request.FILES, instance=EMC_record)
        formset = EMCTestFormSet(request.POST, instance=EMC_record)
        formset_hardware = EMCHardwareFormSet(request.POST, instance=EMC_record)
        formset_software = EMCSoftwareFormSet(request.POST, instance=EMC_record)
        if form.is_valid():
            emc = form.save()
            formset.instance = emc
            formset_hardware.instance = emc
            formset_software.instance = emc
            formset.save()
            formset_hardware.save()
            formset_software.save()
            return redirect('UserAuth:EMC_table')
    else:
        form = EMCAdminForm(instance=EMC_record)
        formset = EMCTestFormSet(instance=EMC_record)
        formset_hardware = EMCHardwareFormSet(instance=EMC_record)
        formset_software = EMCSoftwareFormSet(instance=EMC_record)
    return render (request, 'edit_EMC.html',
                    {'form': form,
                    'formset' : formset,
                    'formset_hardware' : formset_hardware,
                    'formset_software' : formset_software,
                    'editable': True})

@login_required(login_url='UserAuth:login')
def delete_EMC(request, id):
    EMC_record = get_object_or_404(EMC, id=id)
    if request.method == 'POST':
        EMC_record.delete()
        return redirect('UserAuth:EMC_table')
    return render(request, 'EMC_records.html', {'form': EMCAdminForm(instance=EMC_record)})

@login_required(login_url='UserAuth:login')
def download_EUT_Description(request, id):
    EMC_datas = get_object_or_404(EMC, id=id)
    if os.path.exists(EMC_datas.EUT_Description.path):
        response = FileResponse(EMC_datas.EUT_Description.open(), as_attachment=True, filename=EMC_datas.EUT_Description.name.split('/')[-1])
        return response
    else:
        return HttpResponseNotFound('File not found')
    
#E-Lab Part

@login_required(login_url='UserAuth:login')
def view_e_lab(request):
    sort_by = request.GET.get('sort_by', 'Last_Update')
    order = request.GET.get('order', 'desc')
    if order == 'asc':
        Test_datas = E_lab.objects.all().order_by(sort_by)
    else:
        Test_datas = E_lab.objects.all().order_by(f'-{sort_by}')
    context = {
        'Test_datas': Test_datas,
        'current_order': order
    }
    return render(request,'Test_records.html', context=context)

@login_required(login_url='UserAuth:login')
def edit_Test(request, id):
    Test_datas = get_object_or_404(E_lab, id=id)
    if not (request.user.is_superuser or request.user == Test_datas.Requester or request.user == Test_datas.Requested_to):
        form = E_labAdminForm(instance=Test_datas)
        return render(request, 'view_Test.html', {'form': form})
    if request.method == 'POST':
        form = E_labAdminForm(request.POST, request.FILES, instance=Test_datas)
        if form.is_valid():
            form.save()
            return redirect('UserAuth:view_e_lab')
    else: 
        form = E_labAdminForm(instance=Test_datas)
    return render(request, 'edit_Test.html', {'form': form, 'editable': True})

@login_required(login_url='UserAuth:login')
def delete_EMC(request, id):
    Test_Datas = get_object_or_404(E_lab, id=id)
    if request.method == 'POST':
        Test_Datas.delete()
        return redirect('UserAuth:view_e_lab')
    return render(request, 'Test_records.html', {'form': E_labAdminForm(instance=Test_Datas)})

@login_required(login_url='UserAuth:login')
def download_Test_File(request, id):
    Test_datas = get_object_or_404(E_lab, id=id)
    if os.path.exists(Test_datas.Test_Files.path):
        response = FileResponse(Test_datas.Test_Files.open(), as_attachment=True, filename=Test_datas.Test_Files.name.split('/')[-1])
        return response
    else:
        return HttpResponseNotFound('File not found')