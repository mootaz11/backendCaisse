from django.db import models
from datetime import  datetime
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField(default=0.0)
    stock=models.IntegerField(default=1)
    discount=models.BooleanField(default=False)
    offer=models.BooleanField(default=False)
    image = models.ImageField(default='default.png',upload_to='products_picture')

    def __str__(self):
        return  self.name


class Order(models.Model):
    date=models.DateTimeField(default=datetime.now())
    total=models.FloatField(default=0)
    passed=models.BooleanField(default=False)


    def __str__(self):
        return str(self.date)


class Ticket(models.Model):
    date=models.CharField(max_length=30)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    pdf=models.FileField(upload_to='pdfs',null=True,blank=True)

    def __str__(self):
        return str(self.date)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='orderProducts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product')
    quantity = models.IntegerField(default=1)



    def __str__(self):
        return str(self.quantity)



