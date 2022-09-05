from django.contrib import admin
from .models import Bill, BillRows, Customer, Employee, Category, Product

# Register your models here.
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(BillRows)
