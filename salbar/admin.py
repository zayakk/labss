from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug', 'description', 'cat_image')
    prepopulated_fields = {'slug': ('cat_name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'price', 'stock', 'is_available', 'category', 'created_date', 'modified_date')
    list_filter = ('is_available', 'category')
    search_fields = ('product_name', 'description')
    prepopulated_fields = {'slug': ('product_name',)}
admin.site.register(Product, ProductAdmin)