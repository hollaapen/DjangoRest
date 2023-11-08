from django.db import models


# Create your models here.

class Products(models.Model):
    product = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField(default='Description')
    image = models.ImageField(upload_to="products", default="products/product.jpg")

    def __str__(self):
        return self.product


class Students(models.Model):
    product = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField(default='Description')
    image = models.ImageField(upload_to="products", default="product.jpg")

    def __str__(self):
        return self.product