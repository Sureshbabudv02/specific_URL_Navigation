from django.shortcuts import render

# Create your views here.

def husband(request):
    return render(request,'husband.html')