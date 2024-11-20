from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
