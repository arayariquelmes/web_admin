from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"web/index.html")

def personas(request):
    return HttpResponse("Este es el modulo de personas")