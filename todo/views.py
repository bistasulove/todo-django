from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('completed', '-created_at')

    form = TaskForm()


    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


    context = {'tasks' : tasks, 'form' : form }
    
    return render(request, 'todo/list.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'form' : form }

    return render(request, 'todo/update.html', context)

def delete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect("/")

    context = {'task' : task}

    return render(request, 'todo/delete.html', context)