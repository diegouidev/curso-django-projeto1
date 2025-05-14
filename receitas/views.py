from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'receitas/home.html')

def sobre(request):
    return HttpResponse('Estamos na página sobre')

def contato(request):
    return HttpResponse('Estamos na página contato')