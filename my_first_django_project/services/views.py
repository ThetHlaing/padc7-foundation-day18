from django.shortcuts import render
from django.http import HttpResponse
from .models import Service

# Create your views here.
def index(request):
    title = "This is a title"
    all_services = Service.objects.all()
    context = {'title':title,'services': all_services}

    return render(request,'services/index.html',context)

def detail(request,name,id):
    return HttpResponse(f'<h1>{name}</h1><p> Id is {id}</p>')