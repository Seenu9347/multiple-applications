from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Dhoni(request):
    return render(request,'msd.html')

def jadeja(request):
    return HttpResponse('<h1><marquee>india best all rounder</marquee></h1>')
