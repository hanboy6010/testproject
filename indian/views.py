from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'indian/index.html', {})

def post_list(request):
    return render(request, 'indian/post_list.html', {})