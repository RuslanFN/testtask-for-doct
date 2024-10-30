from rest_framework import serializers
from market import models

class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    img = serializers.ImageField()
    class Meta:
        model = models.Category
        fields = ['title','slug' ,'img', 'subcategories']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = ['slug', 'img']