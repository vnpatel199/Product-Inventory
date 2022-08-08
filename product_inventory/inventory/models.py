from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    employee_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.category_name}'

    def get_all_product(self):
        return Product.objects.filter(category=self)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="image")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    gst = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_name}'


class Customer(models.Model):
    customer_name = models.CharField(max_length=60)
    phone_number = models.IntegerField()
    gst_number = models.IntegerField()


class Bill(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    gst_amount = models.DecimalField(max_digits=4, decimal_places=2)


class BillRows(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=4, decimal_places=2)
