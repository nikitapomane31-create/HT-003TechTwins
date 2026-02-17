from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def medi(request):
    return render(request, 'medi.html')