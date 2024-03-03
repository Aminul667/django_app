# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Hello Django, Nice to meet you !')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('Hello, This is about page')
    return render(request, 'about.html')
