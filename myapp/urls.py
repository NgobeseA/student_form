from django.urls import path
from .views import home, about, student_profile, student_list, register_view, welcome_view
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('profile/', student_profile, name="profile"),
    path('student_list/', student_list, name="student_list"),
    path('signup/',register_view, name="signup"),
    path('welcome/', welcome_view, name="welcome"),
    path('profiles/', views.profile_view, name='profiles')
]
