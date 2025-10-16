from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    breadcrumb = [
        ("Home", "/")
    ]
    context = {'name': 'toto', "breadcrumb": breadcrumb}
    return render(request, "index.html", context)