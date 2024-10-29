from django.contrib import admin
from market.models import Product, ImageProduct, Category, SubCategory, Cart, CartItem
# Register your models here.

class ImageProductInline(admin.StackedInline):
    model = ImageProduct
    extra = 3

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
admin.site.register(Cart)
admin.site.register(CartItem)