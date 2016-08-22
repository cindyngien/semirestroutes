from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product
# Create your views here.
def index(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request, 'semirest/index.html', context)
    #display all your products here

def new(request):
    #all this is doing is when it is called in the index.html page, it will render this new product page displaying all of the forms.
    return render(request, 'semirest/newproduct.html')
    #clicking here will bring you to a new page where you can create the products
def create(request):
    #when you click the create button, this is when the form action will get involked and create all the items you had input into the form
    new_product = Product()
    new_product.product_name = request.POST["name"]
    new_product.product_description = request.POST["description"]
    new_product.product_price = request.POST["price"]
    new_product.save()
    return redirect(reverse('myindex'))

def show(request, product_id):
    #this method will simply just show the products for you in a separate page
    context = {
        'product': Product.objects.get(id=product_id)
    }
    return render(request,'semirest/show.html', context)

def edit(request, product_id):
    context = {
        'product': Product.objects.get(id=product_id)
    }
    return render(request,'semirest/edit.html', context)

def update(request, product_id):
    #confusing part... it runs through the edit method, renders the edit.html template, but that is a GET method, the update will be a POST method from within your form
    prod = Product.objects.get(id=product_id)
    prod.product_name = request.POST["name"]
    prod.product_description = request.POST["description"]
    prod.product_price = request.POST["price"]
    prod.save()
    return redirect('myindex')

def destroy(request, product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('myindex')
