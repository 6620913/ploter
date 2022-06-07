from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,"index.html")
def polygon(request):

    return render(request,"components/polygon.html")

def circle(request):

    return render(request,"components/circle.html")