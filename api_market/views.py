from django.shortcuts import render
from api_market import serializers
from market import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from market import models
@api_view(['GET', 'POST'])
def get_categories(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        serializer  = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        serializer  = serializers.ProductsSerializer(products, many=True)
        return Response(serializer.data)

