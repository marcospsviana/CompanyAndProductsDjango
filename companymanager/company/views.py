import pickle

from django.shortcuts import render
from .models import Company, Product


def create_product(request):
    # form = CreateProduct(request.POST)
    #
    # for field in form:
    #     print("Field Error:", field.name, field.errors)
    companies = Company.objects.all()
    companies = pickle.loads(pickle.dumps(companies))

    if request.method == "POST":
        company = request.POST["company"]
        product = request.POST["product"]
        print(f"company  {product}")
        id_company = Company.objects.get(name=company)
        product = Product(company=id_company, name=product)
        product.save()

    return render(request, "create-products.html", context={"companies": companies})


def list_products(request):
    return render(request, "products.html")
