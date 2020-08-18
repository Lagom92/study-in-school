from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def board(request):
    return render(request, 'board.html')


def count_word(request):
    text = request.POST['board_text']
    data = {}
    data['text_length'] = len(text)
    data['text_length_not_empty'] = len(text.replace(" ", ""))

    return render(request, 'count_word.html', data)