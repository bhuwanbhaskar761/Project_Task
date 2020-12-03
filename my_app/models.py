from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    stu_class = models.CharField(max_length=100,null=True)
    roll_no = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.first_name
