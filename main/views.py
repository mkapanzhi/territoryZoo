from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from main.models import Animal, Product, Brand, Article


def get_page(request):
    products_queryset = Product.objects.all().prefetch_related('productcount_set')
    animals = Animal.objects.all()
    products = products_queryset.order_by('-top_product')[:3]
    new_products = products_queryset.order_by('-id')[:10]
    brands = Brand.objects.all()
    articles = Article.objects.all()
    cart_product_form = CartAddProductForm()


    # products2 = Product.objects.filter(name__icontains='р')
    products3 = Animal.objects.filter(product__id=1)
    print(products3)

    context = {
        'animals': animals,
        'products': products,
        'new_products': new_products,
        'brands': brands,
        'articles': articles,
        'cart_product_form': cart_product_form
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
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'basket.html', context)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('main')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('basket')
