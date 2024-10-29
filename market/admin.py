from django.contrib import admin
from market.models import Product, ImageProduct, Category, SubCategory, Cart, CartItem
from django.contrib.auth.models import User
# Register your models here.
UserCart = User
class ImageProductInline(admin.StackedInline):
    model = ImageProduct
    extra = 3


class CartItemInline(admin.StackedInline):
    model = CartItem

class UserInline(admin.StackedInline):
    model = User

class CartAdmin(admin.ModelAdmin):
    list_display = ["user"]
    inlines = [CartItemInline]


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageProductInline]
    prepopulated_fields = {'slug': ('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
