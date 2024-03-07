from django.db import models
from faker import Faker
from django.db import models
import django
import random 
import os
class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    # def __str__(self):
    #     self.title

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'S'

    MEMBERSHIP_CHOICES= [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold')
    ]

    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 50, unique = True)
    phone = models.IntegerField()
    birt_date = models.DateField(null = True)
    membership = models.CharField(max_length=1 , choices= MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)
    # many to many relationship with product
    purchased_product = models.ManyToManyField(Product, related_name= 'customers', blank=True)

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE,'Complete'),
        (PAYMENT_FAILED, 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now = True)
    payment_status = models.CharField(max_length = 1, choices= PAYMENT_STATUS, default= PAYMENT_PENDING)
    customer = models.ForeignKey(Customer,related_name = 'orders', on_delete = models.CASCADE)

#  One to one relationship between Customer and Address
class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)



# creating mock data
# os.environ.setdefault("ABCD", "newsite.settings")
# django.setup()

# fake = Faker()
# NUM_PRODUCTS = 10

# for _ in range(NUM_PRODUCTS):
#     title = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
#     description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
#     price = round(random.uniform(10, 1000), 2)
#     inventory = random.randint(1, 100)
#     product = Product.objects.create(title=title, description=description, price=price, inventory=inventory)
#     print(f"Created product with title: {product.title}")


