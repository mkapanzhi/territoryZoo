from django.shortcuts import render


def get_page_coockie(request):
    print(request.COOKIES.get('color'))

    response = render(request, 'coockie.html')
    response.set_cookie('color_back', request.COOKIES.get('color_js'))
    return response
