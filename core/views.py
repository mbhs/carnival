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


def contact(request):
    return


def dayof(request):
    context = {
        'navbar': ''
    }
    return render(request, 'core/dayof.html', context)
