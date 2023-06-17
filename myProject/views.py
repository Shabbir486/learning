from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    return render(request,'test.html')

def results(request):
    return HttpResponse("You're looking at the results.")