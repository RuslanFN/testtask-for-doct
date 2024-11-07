from django.shortcuts import render
from api_market import serializers
from rest_framework import generics
from market import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from market import models
from rest_framework.pagination import PageNumberPagination
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
    paginator = PageNumberPagination()
    paginator.page_size = 2
    if request.method == 'GET':
        products = models.Product.objects.all()
        page=paginator.paginate_queryset(products, request)
        serializer  = serializers.ProductsSerializer(page, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def get_cart(request):
    if request.method == "GET":
        if IsAuthenticated:
            serializer = serializers.CartSerializer(request.user.Cart)
            return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    if request.method == "POST":
        if IsAuthenticated:
            cart, _ = models.Cart.objects.get_or_create(user=request.user)
            serializer = serializers.CartForUpdateSerializer(instance=cart, data=request.data)
            if serializer.is_valid(raise_exception=True): 
                serializer.save()
                return Response({'post': serializer.data})
            else:
                return Response('Неверные данные', 400)


@api_view(['DELETE'])
def remove_item_cart(request, slug):
    if request.method == "DELETE":
        if IsAuthenticated:
            cart_item = generics.get_object_or_404(request.user.Cart.CartItem, product_id__slug=slug)
            cart_item.delete()
            return Response(status=204)
        