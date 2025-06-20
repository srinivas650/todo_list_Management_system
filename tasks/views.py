from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    tasks=Task.objects.all() 
    context={
        'tasks':tasks.order_by('-id')
    }
    return render(request,'home.html',context)
    
def create_task_view(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        desc=data.get('desc')
        Task.objects.create(tname=name,tdesc=desc)
        return redirect('home')

    return render(request,'create_task.html')

def update_task_view(request,pk):
    try:
        task=Task.objects.get(id=pk)
    except:
        return HttpResponse('<center><h1>Task not found')

    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        desc=data.get('desc')
        task.tname=name
        task.tdesc=desc
        task.save()
        return redirect('home')
    context={
        'task':task,
    }
    return render(request,'update_task.html',context)


def delete_task_view(request,pk):
    try:
        
        task=Task.objects.get(id=pk)
    except:
        return HttpResponse('<center><h1>Task not found')
    task.delete()
    return redirect('home')