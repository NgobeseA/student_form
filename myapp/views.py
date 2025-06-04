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

def student_profile(request):
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
    
def welcome_view(request):
    return render(request, 'welcome.html')

def profile_view(request):
    profile = request.user.student
    print(profile)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
        else:
            form = StudentForm(instance=profile)
        return render(request, 'registration.html', {'form': form, 'profile': profile})