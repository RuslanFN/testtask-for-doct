from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from market.forms import AuthForm
from market.models import Category, ImageProduct, Product, SubCategory
from json import dumps
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
# Create your views here.

def categories(request):
    objects = Category.objects.all()
    return render(request, 'market/categories.html', {'title':'Категории', 'categories':objects})

def products_by_subcategory(request, category, subcategory):
    sub_category = SubCategory.objects.filter(slug=subcategory).first()
    objects = sub_category.products.all()
    return render(request, 'market/products.html', {'title': sub_category.title, 'products':objects})

def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            print(token, _)
        return redirect('/categories')
        
    else: return render(request, 'market/login.html', {'title':'Авторизация', 'form': AuthForm()})
            
        