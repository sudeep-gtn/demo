import os
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
# import Q operator (Query)
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from stores.models import Product
from stores.models import Customer

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Sudeep', 'age':19})
def say_goodmorning(request):
    return HttpResponse("Hello I want to say you Good Morning .....")
# products_to_create = [
#     Product(title='Laptop', description='A powerful laptop for gaming and work.', price=1499.99, inventory=50),
#     Product(title='Tablet', description='A lightweight tablet for entertainment and productivity.', price=399.99, inventory=30),
#     Product(title='Computer', description='A powerful computer for coding and programming.', price=899.99, inventory=30),
#     Product(title='DSLR', description='A Digital Camera for awesome photography.', price=399.99, inventory=30),
#     Product(title='Coffee maker', description='A coffe maker machine for your daily coffee.', price=399.99, inventory=30),
#     # Add more products here as needed
# ]
# Product.objects.bulk_create(products_to_create)


# customer1 = Customer.objects.create(
#     first_name='Sudeep',
#     last_name='Bogati',
#     email='sudeep@example.com',
#     phone=1234567890,
#     birth_date=timezone.now().date(),
#     membership=Customer.MEMBERSHIP_SILVER
# )

# customer2  = Customer.objects.create(
#         first_name='Sodeep',
#         last_name='Chhetry',
#         email='the_sudeep@example.com',
#         phone=1234567890,   
#         birth_date=timezone.now().date(),
#         membership=Customer.MEMBERSHIP_SILVER
#     ),
# customer3 = Customer.objects.create(
#         first_name='John',
#         last_name='Doe',
#         email='john.doe@example.com',
#         phone=1234567890,
#         birth_date=timezone.now().date(),
#         membership=Customer.MEMBERSHIP_SILVER
#     )

def get_prods(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

    # logical operations 
    # ls => less than 
    # gt => greater than 
    # lte => lesst than or equal to 

    # using query operator for logical filer (OR , AND )
    # products = Product.objects.filter(Q(price__gt=500) | Q( description__isnull = False))
    # if(products):
    #     return render(request, 'products.html', {'products':products})
    # else:
    #     HttpResponse("NO PRODUCTS FOUND !")

    # products = Product.objects.all()
    # return render(request, 'products.html', {'products': products})


def delete_all(request):
    Product.objects.all().delete()
    return HttpResponse("Successfully deleted data from the table ")

# def welcome_msg(request):
#     return render(request, 'welcome.html', {'name': 'Sudeep', 'products':get_prods})

