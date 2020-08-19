from django.shortcuts import render
from .models import AiClass
# Create your views here.


def main(request):
    return render(request, 'main.html')

def aiclass(request):
    ai_class = AiClass.objects.all()

    data = {
        'ai_class': ai_class
    }

    return render(request, 'class.html', data)