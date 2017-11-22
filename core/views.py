from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'core/index.html', context)


def instruments(request):
    context = {}
    return render(request, 'core/instruments.html', context)


def organizers(request):
    context = {}
    return render(request, 'core/organizers.html', context)
