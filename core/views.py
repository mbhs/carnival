from django.http import FileResponse
from django.shortcuts import render


def index(request):
    context = {
        'navbar': 'home'
    }
    return render(request, 'core/index.html', context)


def about(request):
    context = {
        'navbar': 'about'
    }
    return render(request, 'core/about.html', context)


def espanol(request):
    context = {
        'navbar': 'espanol'
    }
    return render(request, 'core/espanol.html', context)
