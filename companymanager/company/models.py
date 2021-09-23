from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"


class Product(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ListProducts(models.Model):
    company = models.ForeignKey(
        Company, related_name="company", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.CASCADE
    )
