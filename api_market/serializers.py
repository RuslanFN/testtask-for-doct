from rest_framework import serializers
from market import models
class SubCategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField()
    img = serializers.ImageField()

    class Meta:
        model = models.SubCategory
        fields = ['slug', 'img']


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    img = serializers.ImageField()
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = models.Category
        fields = ['title','slug' ,'img', 'subcategories']

class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.IntegerField()
    subcategories = serializers.