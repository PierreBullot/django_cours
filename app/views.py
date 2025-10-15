from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'name': 'toto'}
    return render(request, "index.html", context)