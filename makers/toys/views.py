from django.shortcuts import render


def index(request):
    return render(request, 'toys/index.html')


def add(request):
    return render(request, 'toys/add.html')
