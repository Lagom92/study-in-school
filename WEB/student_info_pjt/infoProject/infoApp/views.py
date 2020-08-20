from django.shortcuts import render, redirect
from .models import AiClass, AiStudent
# Create your views here.


def main(request):
    return render(request, 'main.html')

def aiclass(request):
    ai_class = AiClass.objects.all()
    data = {
        'ai_class': ai_class
    }
    return render(request, 'class.html', data)

def detail(request, id):
    students = AiStudent.objects.filter(id=id)
    data = {
        'students': students,
        'id': id
    }

    return render(request, 'detail.html', data)

def add(request, id):

    # 나중에 추가

    return render(request, 'add.html')