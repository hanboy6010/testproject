from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'indian/index.html', {})

def indian(request):
    return render(request, 'indian/indian.html', {})