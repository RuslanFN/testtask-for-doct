from django.shortcuts import render
from market.models import Category, ImageProduct
from json import dumps
from django.http import HttpResponse
# Create your views here.

def categories(request):
    Category.objects.all()
    return 