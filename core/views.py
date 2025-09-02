from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentSignUpForm, EducatorSignUpForm

def index(request):
    return render(request, 'index.html')

def register_student(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = StudentSignUpForm()
    return render(request, 'register.html', {'form': form, 'role': 'Student'})

def register_educator(request):
    if request.method == 'POST':
        form = EducatorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = EducatorSignUpForm()
    return render(request, 'register.html', {'form': form, 'role': 'Educator'})
