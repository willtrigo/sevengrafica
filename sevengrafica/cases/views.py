from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Case, Product
from .decorators import enrollment_required

def cases(request):
    allcases = Case.object.all()
    context = {
        'nome':'Seven Gráfica',
        'activecases':'active',
        'cases':allcases,
    }
    return render(request, 'cases/cases.html', context)

@enrollment_required
def products(request, slug):
    product = request.product
    all_products = request.all_products
    context = {
        'nome':'Seven Gráfica',
        'activecases':'active',
        'product':product,
        'all_products':all_products,
    }
    return render(request, 'cases/products.html', context)
