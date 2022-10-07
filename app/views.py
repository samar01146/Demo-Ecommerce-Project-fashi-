from email import message
from itertools import product
from unicodedata import category
from urllib import request
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerProfileForm, CustomerQueryForm, CustomerRegistrationForm, LoginForm, MyPasswordChangeForm, PasswordResetForm, PasswordSetForm
from django.contrib.auth import authenticate, login
from . models import Cart, CustomerQuery, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import Customer, OrderPlaced
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings




# Create your views here.
def home(request):
    man = Product.objects.filter(category="M")
    women = Product.objects.filter(category="W")
    return render(request, "app/index.html", {'man': man, 'women': women })


def contact(request):
    return render(request, 'app/contact.html')


def faq(request):
    return render(request, 'app/faq.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/register.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'congratulations')
        return render(request, 'app/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']   
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        return render(request, 'app/login.html', {'form': form})

@method_decorator(login_required , name="dispatch")
class CustomerQueryView(View):
    def get(self, request):
        form = CustomerQueryForm()
        return render(request, 'app/contact.html', {'form': form})

    def post(self, request):
        form = CustomerQueryForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            reg = CustomerQuery(user=user, name=name,
                                email=email, message=message)
            messages.success(
                request, "we will get back to you soon.............THANK YOU!")
            reg.save()
            # form.save()
        return render(request, 'app/contact.html', {'form': form})
@login_required
def addtocart(request, pk):
    user = request.user
    product =  Product.objects.get(id=pk)
    Cart(user=user, product=product).save()
    return redirect('shop')

def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount =70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount =  amount + shipping_amount
            return render(request, 'app/shopping-cart.html' , {'carts' : cart , 'amount':amount , 'totalamounts' :totalamount})
            
        return render(request, 'app/shopping-cart.html' , {'carts' : cart , 'amount':amount })
    else:
        return render(request, 'app/emptycart.html' )
    
@login_required
def remove_cart(request,pk):
    cart_delete = Cart.objects.get(id=pk)
    cart_delete.delete()
    return redirect('/cart')
                


@login_required
def plus_cart(request , pk):
    cart_add = Cart.objects.get(id=pk)
    cart_add.quantity +=1 
    cart_add.save()
    return redirect('/cart')


@login_required
def minuscart(request,  pk):
    cart_minus = Cart.objects.get(id=pk)
    cart_minus.quantity -=1
    cart_minus.save()
    return redirect('/cart')
    

class ProductView(View):
    def get(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        print("======================================", product)
        return render(request, 'app/product.html', {'product': product})


class ShopView(View):
    def get(self, request):
        man = Product.objects.filter(category='M')
        women = Product.objects.filter(category='W')
        shoes = Product.objects.filter(category='S')
        coat = Product.objects.filter(category='C')
        cap = Product.objects.filter(category='CA')
        bag = Product.objects.filter(category='B')
        return render(request, 'app/shop.html', {'man': man, 'women': women, 'shoes': shoes, 'coat': coat, 'cap': cap, 'bag': bag})


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount =70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            totalamount =  amount + shipping_amount
            return render(request, 'app/check-out.html' , {'add':add, 'cart':cart , 'amount' :amount , 'totalamount':totalamount, 'shipping_amount': shipping_amount})
    else:
        return render(request, 'app/check-out.html' , {'add':add, 'cart':cart , 'amount' :amount ,  'shipping_amount': shipping_amount})


def man(request):
    man = Product.objects.filter(category="M")
    return render(request, 'app/man.html', {'man': man})


def women(request):
    women = Product.objects.filter(category="W")
    return render(request, 'app/women.html', {'women': women})


def shoes(request):
    shoes = Product.objects.filter(category='S')
    return render(request, 'app/shoes.html', {'shoes': shoes})


def coat(request):
    coat = Product.objects.filter(category='C')
    return render(request, 'app/coat.html', {'coat': coat})


def dress(request):
    dress = Product.objects.filter(category='D')
    return render(request, 'app/dress.html', {'dress': dress})

# this is PasswordChangeView Class Based Method


class PasswordChangeView(View):
    def get(self, request):
        form = MyPasswordChangeForm(request.user)
        return render(request, 'app/changepassword.html', {'form': form})

    def post(self, request):
        form = MyPasswordChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
        messages.success(request, "Your Password is successfully Updated")
        return render(request, 'app/changepassword.html', {'form': form})

@method_decorator(login_required , name="dispatch")
class CustomerProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=user, name=name, locality=locality,
                           city=city, zipcode=zipcode, state=state,)
            reg.save()
            messages.success(request, 'Your Form is Submitted Successfully')
        return render(request, 'app/profile.html', {'form': form})


def orderplaced(request):
    user = request.user
    customer = Customer.objects.filter(user=user).first()                                                                                                                                                                                                                                  
    cart = Cart.objects.filter(user=user)
    print("==================================",cart)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return render(request, 'app/payment.html')



    
