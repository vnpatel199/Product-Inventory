from django.contrib import admin
from .models import Employee, Category, Product

# Register your models here.
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Product)
