from email import message
import email
from hmac import new
from django.contrib import admin
from django.contrib.auth.models import User

from .models import CustomerQuery, Product, Customer, Cart, OrderPlaced

# Register your models here.
@admin.register(CustomerQuery)
class AdminCustomerQuery(admin.ModelAdmin):
    list_display = ['id' , 'user', 'name' , 'email' , 'message' ]

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display =['title' , 'selling_price' , 'discounted_price' , 'brand' , 'category' , 'description' , 'product_images']  

@admin.register(Customer)
class AdminCustomerProfile(admin.ModelAdmin):
    list_display = ['id' ,'user' , 'name' , 'locality' ,'add_field', 'city' , 'zipcode', 'state',  ] 



    def add_field(self, obj):
        # newfield = User.objects.filter(email = obj.user.email).values("email")[0]
        newfield = User.objects.filter(email = obj.user.email).first()
        print("=============================================",newfield.email)
        return newfield.email

@admin.register(Cart)                       
class AdminCart(admin.ModelAdmin):
    list_display = ['user' , 'product', 'quantity' ]   

@admin.register(OrderPlaced)                       
class AdminOrderPlaced(admin.ModelAdmin):
    list_display = ['user' , 'customer', 'product'   , 'quantity' , 'orderdate'] 


