from django.db import models
from user.models import Profile
from home.models import Games,Offers
# Create your models here.
class CartItems(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    game=models.ForeignKey(Games,on_delete=models.SET_NULL, null=True)
    date_time=models.DateTimeField(auto_now=True)
    is_ordered = models.BooleanField(default=False)
    ref_code=models.CharField(max_length=8)
    amount=models.FloatField(null=True)
    def __str__(self):
        return "{1}--{0}".format(self.game,self.ref_code)

class RentItemsCart(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    offer=models.ForeignKey(Offers,on_delete=models.SET_NULL, null=True)
    amount=models.FloatField(null=True)
    ref_code=models.CharField(max_length=5)
    duration=models.PositiveSmallIntegerField()
    is_ordered = models.BooleanField(default=False)
    def __str__(self):
        return "{1}-{0}".format(self.offer,self.ref_code)

class Order(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    total=models.FloatField()
    date=models.DateField(auto_now_add=True)
    order_ref_code=models.CharField(max_length=8)
    def __str__(self):
        return "{0}--{1}".format(self.date,self.owner)

class OrderItems(models.Model):
    game=models.ForeignKey(Games,on_delete=models.SET_NULL, null=True)
    date_time=models.DateTimeField(auto_now_add=True)
    ref_code=models.CharField(max_length=8)
    amount=models.FloatField(null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return "{1}--{0}".format(self.game,self.ref_code)

class RentOrder(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    total=models.FloatField()
    date=models.DateField(auto_now_add=True)
    order_ref_code=models.CharField(max_length=8)
    def __str__(self):
        return "{0}--{1}".format(self.date,self.owner)

class RentItems(models.Model):
    game=models.ForeignKey(Games,on_delete=models.SET_NULL,null=True)
    order_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    ref_code=models.CharField(max_length=8)
    amount=models.FloatField(null=True)
    rentorder=models.ForeignKey(RentOrder,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return "{1}--{0}".format(self.game,self.ref_code)


    