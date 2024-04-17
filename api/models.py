from django.db import models


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey('Books', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
