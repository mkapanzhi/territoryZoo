from django.contrib import admin

from .models import Animal, Brand, CategoryProduct, Reviews, Sales, Article, Product, ProductCount, ProductImage

# Register your models here.
admin.site.register(Animal)
admin.site.register(Brand)
admin.site.register(CategoryProduct)
admin.site.register(Reviews)
admin.site.register(Sales)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(ProductCount)
admin.site.register(ProductImage)
