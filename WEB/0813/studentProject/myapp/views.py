from django.shortcuts import render

# Create your views here.


def question(request):

    return render(request, 'question.html')

def answer(request):
    data = {}

    question = request.POST.get('q')
    data['question'] = question
    data['length'] = len(question)

    not_space = len(question.replace(" ", ""))
    data['not_space_length'] = not_space

    return render(request, 'answer.html', data)