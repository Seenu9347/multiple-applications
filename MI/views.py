from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Rohit(request):
    return render(request,'rohit.html')

def SKY(request):
    return HttpResponse('<h1>MRs 360 in india</h1>')
