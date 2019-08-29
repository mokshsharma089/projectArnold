from django.contrib import admin
from orders import models
# Register your models here.
admin.site.register([
    models.CartItems,
    models.Order,
    models.OrderItems,
    models.RentItemsCart,
    models.RentOrder,
    models.RentItems
])