from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    #password=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    



class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.ImageField()
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart_id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        cartitems=self.cartitems_set.all()
        total=sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_itemtotal(self):
        cartitems=self.cartitems_set.all()
        total=sum([item.quantity for item in cartitems])
        
        return total


class Cartitems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    def __str__(self):
        return self.product.name
    
    @property
    def get_total(self):
        total=self.quantity * self.product.price
        if total <= 0:
            self.delete()
        return total
  

    
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    #cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    cart=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=30)
    def __str__(self):
        return self.address
    
class Order(models.Model):
    ORDER_STATUS = ((0, 'Pending'),(1,'Shipped'),(2, 'Completed'), (3, 'Return'))
    cartt=models.ForeignKey(Cart,on_delete=models.CASCADE)
    status=models.SmallIntegerField(choices=ORDER_STATUS)
    
