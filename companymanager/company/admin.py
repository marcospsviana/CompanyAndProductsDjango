from django.contrib import admin
from companymanager.company.models import Company, Product, ListProducts

# Register your models here.
@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(ListProducts)
class AdminListProduct(admin.ModelAdmin):
    list_display = ["company", "product"]
