from django.db import models





class Company(models.Model):
    name = models.CharField(max_length=60)


class Product(models.Model):
    name = models.CharField(max_length=150)

class ListProducts(models.Model):
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)

