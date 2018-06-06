from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import GameSet

def index(request):
    return render(request, 'indian/index.html', {})

def indian(request):
    return render(request, 'indian/indian.html', {'game': GameSet})


