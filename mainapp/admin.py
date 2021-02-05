from django.contrib import admin

from mainapp.models import ProductCategory, Product, Menu

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Menu)
