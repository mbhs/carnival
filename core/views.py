from django.shortcuts import render


def index(request):
    context = {
        'navbar' : 'home'
    }
    return render(request, 'core/index.html', context)

def about(request):
    context = {
        'navbar' : 'about'
    }
    return render(request, 'core/about.html', context)

def contact(request):
    context = {
        'navbar' : 'contact'
    }
    return render(request, 'core/contact.html', context)

def instruments(request):
    context = {}
    return render(request, 'core/instruments.html', context)

def organizers(request):
    context = {}
    return render(request, 'core/organizers.html', context)
