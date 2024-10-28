from django.shortcuts import render
from market.models import Category, ImageProduct, Product, SubCategory
from json import dumps
from django.http import HttpResponse
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
        