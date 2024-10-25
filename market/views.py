from django.shortcuts import render
from market.models import Category, ImageProduct
from json import dumps
from django.http import HttpResponse
# Create your views here.

def categories(request):
    for image in ImageProduct.objects.all():
        print(image.get_absolute_url())
    return HttpResponse(str(Category.objects.all()  ))