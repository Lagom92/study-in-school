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
    students = AiStudent.objects.filter(class_number=id)
    data = {
        'students': students,
        'id': id
    }

    return render(request, 'detail.html', data)

def add(request, id):
    if request.method == 'POST':
        res = request.POST

        AiStudent.objects.create(
            name = res['name'],
            class_number = id,
            introduce = res['introduce'],
            github = res['github']
        )
        
        return redirect('detail', id)

    return render(request, 'add.html')

def student(request, student_id):
    student = AiStudent.objects.get(id=student_id)
    data = {
        'student': student
    }

    return render(request, 'student.html', data)

def edit(request, student_id):
    if request.method == 'POST':
        student = AiStudent.objects.filter(id=student_id)
        student.update(
            name = request.POST['name'],
            introduce = request.POST['introduce'],
            github = request.POST['github']
        )
        
        return redirect('student', student_id)

    student = AiStudent.objects.get(id=student_id)
    data = {
        'student': student
    }

    return render(request, 'edit.html', data)

def delete(request, class_id, student_id):
    student = AiStudent.objects.get(id=student_id)
    student.delete()

    return redirect('detail', class_id)
