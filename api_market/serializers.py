from rest_framework import serializers
from market import models
class CategoryOnlySerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    img = serializers.ImageField(read_only=True)

    class Meta:
        model = models.Category
        fields = ['title','slug' ,'img']
class SubCategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    img = serializers.ImageField(read_only=True)

    class Meta:
        model = models.SubCategory
        fields = ['slug', 'img']

class ImageSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(read_only=True)

    class Meta:
        model = models.ImageProduct
        fields = ['img']

class SubCategoryAndCategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    img = serializers.ImageField(read_only=True)
    categoty_id = CategoryOnlySerializer()
    class Meta:
        model = models.SubCategory
        fields = ['slug', 'img', 'categoty_id']

class CategoryOnlySerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    img = serializers.ImageField(read_only=True)

    class Meta:
        model = models.Category
        fields = ['title','slug' ,'img']

class CategoryFullSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    img = serializers.ImageField(read_only=True)
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = models.Category
        fields = ['title','slug' ,'img', 'subcategories']

class ProductsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    sub_category_id = SubCategoryAndCategorySerializer(read_only=True)

    class Meta:
        model = models.Product
        fields = ['title', 'slug', 'price', 'images', 'sub_category_id']


class CartItemSerializer(serializers.ModelSerializer):
    product_id = ProductsSerializer(read_only=True)
    count = serializers.IntegerField(read_only=True)
    amount = serializers.SerializerMethodField()
    class Meta:
        model = models.CartItem
        fields = ['product_id', 'count', 'amount']

class CartSerializer(serializers.ModelSerializer):
    CartItem = CartItemSerializer()
    class Meta:
        model = models.Cart
        fields = ['CartItem']