from django.urls import path
from .views import home, about, student_registration, student_list

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('registration/', student_registration, name="student_registration"),
    path('student_list/', student_list, name="student_list"),
]
