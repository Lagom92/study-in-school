from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AiClass(models.Model):
    number = models.IntegerField()
    teacher = models.CharField(max_length=25)
    room = models.CharField(max_length=25)
    

class AiStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    participate_class = models.ForeignKey(AiClass, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=50)
    github = models.CharField(max_length=250)


class StudentPost(models.Model):
    writer = models.ForeignKey(AiStudent, on_delete=models.SET_NULL, null=True, related_name='post')
    introduce = models.TextField()
