from email.policy import default
from itertools import product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomerQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=200)


CATEGORY_CHOICES =(
    ('M' , 'man'),
    ('W' , 'Women'),
    ('S' , 'shoes'),
    ('C' , 'coat'),
    ('CA' , 'cap'),
    ('B' , 'bag')

)

class Product(models.Model):
    title = models.CharField(max_length =100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    brand = models.CharField(max_length = 50)
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=2)
    description = models.TextField()
    product_images = models.ImageField(upload_to = 'productimg/')
    
    def __str__(self):
        return str(self.id)

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length =200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length= 30)
    zipcode = models.IntegerField()
    state = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    orderdate = models.DateField(auto_now_add=True) 
    def __str__(self):
        return str(self.id)

