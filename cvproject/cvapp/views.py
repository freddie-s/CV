from django.shortcuts import render
from django.http import HttpResponse

def cv(request):
    return render(request, "cv.html")
# Create your views here.
