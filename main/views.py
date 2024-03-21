from django.shortcuts import render

from main.models import Animal


# Create your views here.



def get_page(request):
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }
    return render(request, 'index.html', context)

