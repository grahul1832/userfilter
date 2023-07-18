from django.shortcuts import render


# Create your views here.

def usdf(request):
    d={'name': 'Rahul'}
    return render(request,'usdf.html',d)
