from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    html = "This is just a dummy page"
    return HttpResponse(html)
