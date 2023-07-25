from django.contrib import admin
from .models import *
# admin.site.register(Banner)


class BrandAdmin(admin.ModelAdmin):
	list_display=('id','title','image_tag')
admin.site.register(Brand,BrandAdmin)
admin.site.register(Size)


class ProductAttribute_TabularInline(admin.TabularInline):
    model = ProductAttribute


class Product_admin(admin.ModelAdmin):
    inlines = [ProductAttribute_TabularInline]
    list_display=('id','title','category','brand','status','is_featured')
    list_editable=('status','is_featured')
admin.site.register(Product,Product_admin)



class BannerAdmin(admin.ModelAdmin):
	list_display=('id','alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display=('id','title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
	list_display=('id','title',)
admin.site.register(Color,ColorAdmin)

class QuantityAdmin(admin.ModelAdmin):
	list_display=('id','title',)
admin.site.register(Quantity,QuantityAdmin)


# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','product','price','color','size')
    list_filter = ('product','price','color','size' )
    list_editable = ('price','color','size' )
    search_fields = ('product','price','color','size')
    list_per_page = 25
admin.site.register(ProductAttribute,ProductAttributeAdmin)

# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)


admin.site.register(Wishlist)


class UserAddressBookAdmin(admin.ModelAdmin):
	list_display=('user','address','status')
admin.site.register(UserAddressBook,UserAddressBookAdmin)