from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Student
from .forms import StudentForm, RegistrationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def student_list(request):
    
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_registration(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'registration.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})
