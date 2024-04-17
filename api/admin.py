from django.contrib import admin

from api.models import Author, Books, Shop

# Register your models here.
admin.site.register(Shop)
admin.site.register(Books)
admin.site.register(Author)