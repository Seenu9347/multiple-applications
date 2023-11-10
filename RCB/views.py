from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def ABD(request):
    return HttpResponse('<h1><marquee>MRs 360</marqiuee></h1>')