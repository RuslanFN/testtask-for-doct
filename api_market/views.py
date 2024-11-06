from django.shortcuts import render
from api_market import serializers
from market import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from market import models
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
@api_view(['GET', 'POST'])
def get_categories(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        serializer  = serializers.CategoryFullSerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        serializer  = serializers.ProductsSerializer(products, many=True)
        return Response(serializer.data)
@api_view(['GET', 'POST'])
def get_cart(request):
    if request.method == "GET":
        if IsAuthenticated:
            serializer = serializers.CartSerializer(request.user.Cart)
            return Response(serializer.data)
    if request.method == "POST":
        if IsAuthenticated:
            print(request.data)
            
            serializer = serializers.CartItemForUpdate(instance=request.user.Cart, data=request.data)
            print(serializer.initial_data)

            if serializer.is_valid(raise_exception=True):
                serializer.create(**request.data)
                serializer.save()
                return Response({'post': serializer.data})
            else:
                return Response(404)

