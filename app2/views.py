from django.shortcuts import render

# Create your views here.

def wife(request):
    return render(request,'wife.html')