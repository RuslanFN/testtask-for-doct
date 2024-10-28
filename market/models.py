from django.db import models
from django.shortcuts import reverse
# Create your models here.

def validate_price(value):
        if value <= 0:
            raise ValueError('Цена должна быть положительное')

class Category(models.Model):
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=False)
    img = models.ImageField(upload_to=f"images%y%m%d")

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=False)
    img = models.ImageField(upload_to=f"images%y%m%d")
    categoty_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("products", args=(self.categoty_id.slug, self.slug))


class Product(models.Model):

    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=False)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[validate_price], null=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products", kwargs={'slug':self.slug})

    

class ImageProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    img = models.ImageField(upload_to=f"images%y%m%d")

    def get_absolute_url(self):
        return self.img.url


