from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from market.forms import AuthForm
from market.models import Category, ImageProduct, Product, SubCategory, Cart, CartItem
from json import dumps
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.db.models import F
# Create your views here.

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/categories')
    
    return HttpResponse(status=404)

def categories(request):
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
        return render(request, 'market/cart.html', {'cart':request.user.Cart.CartItem.all()})
    else:
        return HttpResponse(status=404)
    
def remove_item_cart(request, product_slug):
    if request.user.is_authenticated:
        request.user.Cart.CartItem.get(product_id__slug=product_slug).delete()
        return redirect('/cart')
    else:
        return HttpResponse(status=404)
def add_to_cart(request, product_slug):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        print(cart)
        item = cart.CartItem.filter(product_id__slug = product_slug)
        if item.exists():
            print(item.update(count=F('count')+1))
        else:
            CartItem.objects.create(cart=cart, product_id = Product.objects.get(slug=product_slug))
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse(status=404)
def redusce_to_cart(request, product_slug):
    if request.user.is_authenticated:
        item = request.user.Cart.CartItem.filter(product_id__slug = product_slug)
        count = item.first().count
        if count > 1:
            item.update(count=count-1)  
        return redirect('/cart')
    else:
        return HttpResponse(status=404)

