from django.db import models
from datetime import datetime

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=20, default="")
    father_name = models.CharField(max_length=20, default="")
    dob = models.DateField(max_length=10, default=datetime.today())
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=15, default="")
    pin = models.IntegerField(default="")
    mobile = models.BigIntegerField(default="")
    email = models.EmailField(max_length=30)
    standard = (
        ('5', 'Five'),
        ('6', 'Six'),
        ('7', 'Seven'),
        ('8', 'Eight'),
        ('9', 'Nine'),
        ('10', 'Ten'),
    )
    class_opted = models.CharField(max_length=2, choices=standard)
    marks = models.CharField(max_length=3, default="")
    date_enrolled = models.DateTimeField(auto_now_add=True)

