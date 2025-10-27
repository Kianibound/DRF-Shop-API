from django.contrib import admin
from .models import Product, Order, OrderItem
from api.models import User


class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

admin.site.register(Order, OrderAdmin)
admin.site.register(User)
admin.site.register(Product)
