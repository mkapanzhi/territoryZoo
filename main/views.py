from django.shortcuts import render

from main.models import Animal, Product, Brand, Article


def get_page(request):
    products_queryset = Product.objects.all().prefetch_related('productcount_set')
    animals = Animal.objects.all()
    products = products_queryset.order_by('-top_product')[:3]
    new_products = products_queryset.order_by('-id')[:10]
    brands = Brand.objects.all()
    articles = Article.objects.all

    # products2 = Product.objects.filter(name__icontains='р')
    products3 = Animal.objects.filter(product__id=1)
    print(products3)

    context = {
        'animals': animals,
        'products': products,
        'new_products': new_products,
        'brands': brands,
        'articles': articles
    }
    return render(request, 'index.html', context)


def get_result_search(request):
    context = {}
    # if request.method == 'POST':
    #     if len(request.POST.get('search')) > 2:
    #         result = Product.objects.filter(name__icontains=request.POST.get('search'))
    #         print(request.POST.get('search'))
    #         context['result'] = result
    #         print(result)
    products_search2 = Product.objects.filter(description__icontains='Описание')
    print(request.POST.get('search'))
    print(products_search2)
    if request.method == 'POST':
        if request.POST.get('search'):
            if len(request.POST.get('search')) >= 3:
                products_search = Product.objects.filter(price__lte=request.POST.get('search'))
                context['result'] = products_search
                print(products_search)
        else:
            context['error'] = 'Введите более 3 символов'
    return render(request, 'result_search.html', context)

def get_basket(request):
    return render(request, 'basket.html')
