from django.db import models

# Create your models here.
class AiClass(models.Model):
    number = models.IntegerField()
    teacher = models.CharField(max_length=25)
    room = models.CharField(max_length=25)
    student_count = models.IntegerField()


class AiStudent(models.Model):
    name = models.CharField(max_length=50)
    class_number = models.IntegerField()
    age = models.IntegerField()
    introduce = models.TextField()
    github = models.CharField(max_length=250)
    blog = models.CharField(max_length=250)
    sns = models.CharField(max_length=250)