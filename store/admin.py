from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('user','name','email')
admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:70px"/>'.format(obj.image.url))
    list_display=('name','price','image_tag')
admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=('customer','cart_id','completed')
admin.site.register(Cart,CartAdmin)


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product','quantity')
admin.site.register(Cartitems,CartItemsAdmin)

class ShipAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'cart','address','city','state','zipcode')
admin.site.register(ShippingAddress,ShipAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['cartt']
admin.site.register(Order,OrderAdmin)