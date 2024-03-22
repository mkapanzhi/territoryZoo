from django.shortcuts import render

from main.models import Animal, Product


def get_page(request):
    products_queryset = Product.objects.all().prefetch_related('productcount_set')
    animals = Animal.objects.all()
    products = products_queryset.order_by('-top_product')[:3]
    new_products = products_queryset.order_by('-id')[:10]
    context = {
        'animals': animals,
        'products': products,
        'new_products': new_products
    }
    return render(request, 'index.html', context)
