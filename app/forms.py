from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext , gettext_lazy as _
from.models import Customer
from .models import CustomerQuery

# create form from here
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput )
    password2 = forms.CharField(label="confirmpassword" , widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1' , 'password2']
        label = {'email': 'Email'}
        widget = {'username' : forms.TextInput}

class LoginForm(forms.Form):
    username = UsernameField()
    password =forms.CharField(widget=forms.PasswordInput())

class CustomerQueryForm(forms.ModelForm):
    class Meta:
        model = CustomerQuery
        fields = [ 'name' , 'email' , 'message']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"), strip=False, widget=forms.PasswordInput())
    new_password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(),
    help_text = password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm Password"), strip=False, widget=forms.PasswordInput())


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields = [ 'name' ,'locality', 'city', 'zipcode', 'state' ]


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField()
    label = {'email' : 'email'} 

class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(),
    help_text = password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(widget=forms.PasswordInput())
    label = {'new_password1': 'Password' , 'new_password2' : 'Confirm Password'}