from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    gender_choices = [
        ('','SELECT GENDER'),
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        ('PREFER NOT TO SAY', 'prefer not to say'),
    ]
    
    first_name = models.CharField(max_length=100)
    middle_name =models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=gender_choices)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
