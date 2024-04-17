from django.db import models


class Animal(models.Model):  # Животное
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='animals/')

    def __str__(self):
        return self.name


class Product(models.Model):  # Товар
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_preview = models.ImageField(upload_to='products/')
    description = models.TextField()
    animal = models.ManyToManyField('Animal')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE)
    sales = models.ForeignKey('Sales', on_delete=models.SET_NULL, null=True, blank=True)
    top_product = models.PositiveIntegerField(default=0)  # счетчик покупок товара

    def __str__(self):
        return f'{self.name}'


class CategoryProduct(models.Model):  # Категории
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sales(models.Model):  # Акции
    sale_name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    image = models.ImageField(upload_to='sales/')
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()

    def __str__(self):
        return self.sale_name


class ProductImage(models.Model):  # Картинки
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.product.name


class Brand(models.Model):  # Бренд
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name


class ProductCount(models.Model):  # Количество и фасовка продукта
    CHOICES = {
        'шт': 'шт',
        'кг': 'кг',
        'л': 'л',
    }
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.FloatField()
    unit = models.CharField(max_length=20, choices=CHOICES)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name


class Article(models.Model):  # Статьи
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='articles/')
    description = models.TextField()
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    read_time = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title


class Reviews(models.Model):  # Отзывы
    owner = models.CharField(max_length=100)
    description = models.TextField()
    email = models.CharField(max_length=50)
    pet = models.CharField(max_length=50)

    def __str__(self):
        return self.owner
