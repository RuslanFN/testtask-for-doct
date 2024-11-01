"""
URL configuration for sarafan_market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api_market import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from market.views import categories, products_by_subcategory, login_user, logout_user, get_cart, remove_item_cart, add_to_cart, redusce_to_cart
urlpatterns = [
    path('api/products/', views.get_products),
    path('api/categories/', views.get_categories),
    path('removeitemcart/<slug:product_slug>', remove_item_cart, name='removeitemcart'),
    path('addtocart/<slug:product_slug>', add_to_cart, name='addtocart'),
    path('reduscetocart/<slug:product_slug>', redusce_to_cart, name='reduscetocart'),
    path('cart/', get_cart, name='cart'),
    path('admin/', admin.site.urls),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('categories', categories, name='categories'),
    path('products/<slug:category>/<slug:subcategory>', products_by_subcategory, name='products')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


