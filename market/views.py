from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from market.forms import AuthForm
from market.models import Category, ImageProduct, Product, SubCategory, Cart, CartItem
from json import dumps
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
# Create your views here.

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/categories')
    
    return HttpResponse(status=404)

def categories(request):
    get_cart(request)
    objects = Category.objects.all()
    return render(request, 'market/categories.html', {'title':'Категории', 'categories':objects})

def products_by_subcategory(request, category, subcategory):
    sub_category = SubCategory.objects.filter(slug=subcategory).first()
    objects = sub_category.products.all()
    return render(request, 'market/products.html', {'title': sub_category.title, 'products':objects})

def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            Token.objects.get_or_create(user=user)
            login(request, user)
        return redirect('/categories')
        
    else: 
        logout(request)
        return render(request, 'market/login.html', {'title':'Авторизация', 'form': AuthForm()})
            
    
def get_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)
        