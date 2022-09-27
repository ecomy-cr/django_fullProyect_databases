from django.shortcuts import render

# Create your views here.

def homeOf(request):
    return render(request, "homeOf.html")