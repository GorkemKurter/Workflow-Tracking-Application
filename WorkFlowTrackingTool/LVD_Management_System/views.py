from django.shortcuts import render
from .models import Component_Request,Component
# Create your views here.

def component_requests(request):
    component_requests = Component_Request.objects.all()
    return render(request, 'component_requests.html', 
                  {'component_requests': component_requests})
    
def component(request):
    component = Component.objects.all()
    return render(request,'components.html',{'components':component})
    