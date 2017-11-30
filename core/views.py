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


def contact(request):
    context = {
        'navbar': 'contact'
    }
    return render(request, 'core/contact.html', context)


def espanol(request):
    return FileResponse(open('static/espanol.pdf', 'rb'), content_type='application/pdf')

