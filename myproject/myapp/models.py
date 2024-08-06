from django.db import models

class Student(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    student_class = models.CharField(max_length=10)
    section=models.CharField(max_length=2,default='A')
    phone_number = models.CharField(max_length=15)  # Ensure enough length for phone numbers
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    username=models.CharField(max_length=20,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    teacher_class=models.IntegerField()
    subject=models.CharField(max_length=20)
    ph_number=models.IntegerField()

    def __str__(self):
      return self.name