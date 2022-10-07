from re import template
from django.urls import path
from .forms import MyPasswordChangeForm
from app import views
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings
from app.forms import PasswordResetForm,  PasswordSetForm


urlpatterns = [
    path('', views.home , name="home"),
    path('contact/', views.CustomerQueryView.as_view() , name="contact"),
    path('faq/', views.faq , name="faq"),
    path('accounts/login/', views.LoginView.as_view() ,name="login"),
    path('registration/', views.CustomerRegistrationView.as_view() , name="registration"),
    path('shop/', views.ShopView.as_view() , name="shop"),
    path('cart/', views.showcart , name="cart"),
    path('add-to-cart/<int:pk>', views.addtocart , name="addtocart"),
    path('removecart/<int:pk>' , views.remove_cart , name="removecart"),
    path('pluscart/<int:pk>' , views.plus_cart, name= "pluscart" ),
    path('minuscart/<int:pk>' , views.minuscart, name= "minuscart" ),
    path('product/<int:pk>', views.ProductView.as_view() , name="product"),
    path('checkout/', views.checkout , name="checkout"),
    path('orderplaced/', views.orderplaced , name="orderplaced"),
    # path('payment/', views.PaymentView.as_view() , name="payment"),
    path('logout/' , auth_view.LogoutView.as_view(next_page='login'), name= "logout"),
    path('shoes/' , views.shoes, name= "shoes"),    
    path('coat/' , views.coat, name= "coat"),
    path('dress/' , views.dress, name= "dress"),
    # path('shopping/' , views.shoping, name="shopping"),
    # this is URL based Password change View 
    # path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name ="app/changepassword.html", form_class= MyPasswordChangeForm, success_url= '/changepassworddone/'), name="changepassword"),
    # path('changepassworddone/', auth_view.PasswordChangeDoneView.as_view(template_name= "app/changepassworddone.html"), name= "changepassworddone" ),
    path('changepassword/' , views.PasswordChangeView.as_view(), name="changepassword"),
    path('profile/', views.CustomerProfileView.as_view(), name= "profile" ),
    path('man/', views.man, name= "man" ),
    path('women/', views.women, name= "women" ),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name = 'app/passwordreset.html', form_class=PasswordResetForm), name = 'passwordreset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name = 'app/passwordresetdone.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name = 'app/passwordresetconfirm.html', form_class=PasswordSetForm), name = 'password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name = 'app/passwordchangedone.html'), name = 'password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)