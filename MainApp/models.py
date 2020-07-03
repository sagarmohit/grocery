from django.db import models

class Userdata(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Products(models.Model):
    AMOUNT = (
        ('100g' , '100g'),
        ('250g' , '250g'),
        ('500g' , '500g'),
        ('1Kg' , '1Kg'),
        ('2Kg' , '2Kg'),
        ('5Kg' , '5Kg'),
        ('10Kg' , '10Kg')
    )
    CATEGORY =  (
        ('vegetables' , 'vegetables'),
        ('fruits' , 'fruits'),
        ('bakery' , 'bakery'),
        ('dairy' , 'dairy'),
        ('deepfreezed' , 'deepfreezed'),
        ('grocery', 'grocery')
    )
    productcode = models.CharField(max_length=20)
    category = models.CharField(max_length=60 , choices=CATEGORY)
    name = models.CharField(max_length=60)
    price = models.FloatField(max_length=10)
    offerprice = models.FloatField(max_length=10)
    amount = models.CharField(max_length=20, choices=AMOUNT)
    image = models.ImageField(upload_to='productspics')
    offer = models.BooleanField(default=False)
# this thing helps in display name in admin site
    def __str__(self):
        return self.name


class Cart(models.Model):
    username = models.CharField(max_length=60)
    productcode = models.CharField(max_length=20)
    category = models.CharField(max_length=60)
    price = models.FloatField(max_length=20)
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='cartimages')
    amount = models.CharField(max_length=20)


class CategorySelected(models.Model):
    username = models.CharField(max_length=60)
    category = models.CharField(max_length=60)