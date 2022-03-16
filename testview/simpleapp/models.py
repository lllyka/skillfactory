from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse
from django.core.cache import cache

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0.0, 'Price should be >= 0.0')])
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    # допишем свойство, которое будет отображать, есть ли товар на складе
    @property
    def on_stock(self):
        return self.quantity > 0

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/products/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его


    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/products/{self.id}'


    # категории товаров: именно на них ссылается модель товара
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'