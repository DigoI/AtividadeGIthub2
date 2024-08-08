from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse

def rodrigo_view(request):
    return HttpResponse("Página do Rodrigo")
