from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('category-list',views.category_list,name='category-list'),
    path('brand-list',views.brand_list,name='brand-list'),
    path('product-list',views.product_list,name='product-list'),
    path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    path('brand-product-list/<int:brand_id>',views.brand_product_list,name='brand-product-list'),
]

