from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Case, Product

def enrollment_required(view_func):
    def _wrapper(request, *args, **kwargs):
        slug = kwargs['slug']
        product = get_object_or_404(Case, slug=slug)
        all_products = Product.objects.filter(case__name=product.name)
        request.product = product
        request.all_products = all_products
        return view_func(request, *args, **kwargs)
    return _wrapper
