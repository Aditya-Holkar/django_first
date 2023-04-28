from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
    
#     return render(request,'index.html')

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')