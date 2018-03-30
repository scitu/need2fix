import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.models import Task

#@login_required
def task_list(request):
    return render(request, 'app/task_list.html')

@login_required
def task_add(request):
    return render(request, 'app/task_add.html')

@login_required
def task_detail(request, pk):
    context = {'pk': pk}
    return render(request, 'app/task_detail.html', context)


def home(request):
    return render(request, 'app/home.html')