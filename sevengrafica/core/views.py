from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from sevengrafica.cases.models import Product


def home(request):
    allcases = Product.objects.random(6)
    context = {
        'nome':'Seven Gráfica',
        'activehome':'active',
        'cases':allcases
    }

    return render(request, 'core/home.html', context)

def contact(request):
    context = {
        'nome':'Seven Gráfica',
        'activecontato':'active'
    }
    return render(request, 'core/contato.html', context)

def clients(request):
    context = {
        'nome':'Seven Gráfica',
        'activeclientes':'active'
    }
    return render(request, 'core/cliente.html', context)

def aboutus(request):
    context = {
        'nome':'Seven Gráfica',
        'activesobrenos':'active'
    }
    return render(request, 'core/sobrenos.html', context)

def redirect_from_newsleter(request, **kwargs):
    return redirect('/')
