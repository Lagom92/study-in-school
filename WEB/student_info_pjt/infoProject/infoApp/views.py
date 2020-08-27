from django.shortcuts import render, redirect
from .models import AiClass, AiStudent
from django.contrib.auth.models import User
from django.contrib import auth
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
    students = AiStudent.objects.filter(user=id)
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


def signup(request):
    SIGNUP_ERROR_MSG = {
        'data_empty': '데이터를 입력해주세요.',
        'username_duplication': 'id가 이미 존재합니다.',
        'email_duplication': 'email이 이미 존재합니다.',
        'pw_check_diff': '비밀번호가 다릅니다.'
    }
    context = {
        'error_state': False,
        'error_msg': ''
    }

    if request.method == 'POST':
        userId = request.POST['userId']
        password = request.POST['password']
        password_check = request.POST['password_check']

        #
        username = request.POST['username']
        username = request.POST['github']
        username = request.POST['class_num']

        user_id = User.objects.filter(user=userId)

        if user_id and password and password_check:
            if len(user_id) == 0:
                if password == password_check:
                    user = User.objects.create_user(
                        user=user_id,
                        password=password
                    )
                    auth.login(request, user)
                    return render(request, 'signup.html')
                else:
                    # 비밀번호와 비밀번호 확인번호가 다름
                    context['error_state'] = True
                    context['error_msg'] = SIGNUP_ERROR_MSG['pw_check_diff']
            else:
                # 이미 같은 username이 존재함
                context['error_state'] = True
                context['error_msg'] = SIGNUP_ERROR_MSG['username_duplication']
        else:
            # 내용을 입력하지 않음
            context['error_state'] = True
            context['error_msg'] = SIGNUP_ERROR_MSG['data_empty']

    return render(request, 'signup.html', context)
    

def login(request):
    LOGIN_ERROR_MSG = {
        'empty': '내용을 입력하세요',
        'is_no_user': '존재하지 않은 ID입니다.'
    }
    context = {
        'error_state': False,
        'error_msg': ''
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username)\
        
        if username and password:
            if len(user) != 0:
                user = auth.authenticate(
                    username=username,
                    password=password
                )
                if user:
                    auth.login(request, user)

                    return redirect('main')
            else:
                context['error_state'] = True
                context['error_msg'] = LOGIN_ERROR_MSG['is_no_user']
        else:
            context['error_state'] = True
            context['error_msg'] = LOGIN_ERROR_MSG['empty']

    return render(request, 'login.html', context)


def logout(request):
    
    auth.logout(request)

    return redirect('main')