from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login as alogin,authenticate,logout as dlogout
from django.contrib.auth.decorators import login_required
from LVD_Management_System.models import Component_Request,Component
from LVD_Management_System.forms import Component_RequestAdminForm, ComponentAdminForm

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
            messages.error(request, 'err')
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
    component_requests = Component_Request.objects.all()
    return render(request, 'component_requests.html', {'component_requests': component_requests})

@login_required(login_url='UserAuth:login')
def edit_component_request(request, id):
    component_request = get_object_or_404(Component_Request, id=id)
    
    if request.user != component_request.R_Requester and not request.user.is_superuser:
        form = Component_RequestAdminForm(instance=component_request)
        return render(request, 'view_component_request.html', {'form': form})
    
    if request.method == 'POST':
        form = Component_RequestAdminForm(request.POST, instance=component_request)
        if form.is_valid():
            form.save()
            return redirect('UserAuth:component_requests')
    else:
        form = Component_RequestAdminForm(instance=component_request)
    return render(request, 'edit_component_request.html', {'form': form, 'editable': True})

@login_required
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

@login_required
def delete_component_request(request, id):
    component_request = get_object_or_404(Component_Request, id=id)
    if request.method == 'POST':
        component_request.delete()
        return redirect('UserAuth:component_requests')
    return render(request, 'edit_component_request.html', {'form': Component_RequestAdminForm(instance=component_request)})

#LVD Components Part

@login_required
def component(request):
    component = Component.objects.all()
    return render(request,'components.html',{'components':component})

@login_required
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
        
@login_required
def add_component(request):
    if request.method == 'POST':
        form = ComponentAdminForm(request.POST)
        if form.is_valid():
            component = form.save(commit=False)
            component.save()
            return redirect('UserAuth:component')
    else:
        form = ComponentAdminForm()
    return render(request, 'add_components.html', {'form': form})

@login_required
def delete_component(request, id):
    component = get_object_or_404(Component, id=id)
    if request.method == 'POST':
        component.delete()
        return redirect('UserAuth:component')
    return render(request, 'components.html', {'form': ComponentAdminForm(instance=component)})