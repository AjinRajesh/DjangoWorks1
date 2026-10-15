from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    course=models.CharField(max_length=20)
    marks=models.IntegerField()

class Course(models.Model):
    mode_choices=(('offline','OFFLINE'),('online','ONLINE'))#first value(online) in one pair is storedin db and second value(ONLINE) is shown in display
    course_name=models.CharField(max_length=20)
    instructor=models.CharField(max_length=20)
    fee=models.IntegerField()
    duration=models.CharField(max_length=20)
    mode=models.CharField(choices=mode_choices)
