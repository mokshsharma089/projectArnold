from django.shortcuts import render, get_object_or_404
from orders import models
from user.models import Profile
from home.models import Games,Offers
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
import random,string
from django.shortcuts import redirect
from django.urls import reverse
from datetime import timedelta,date
# Create your views here.
@login_required
def AddToCart(request,game_id):
    user_profile = request.user.profile
    game = Games.objects.get(id=game_id)
    cart_item,status= models.CartItems.objects.get_or_create(game=game,amount=game.price,ref_code=''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)]),owner=user_profile)
    if status:
        cart_item.save()
    return HttpResponseRedirect('/home')
@login_required
def show_cart(request):
    cart_items=models.CartItems.objects.filter(owner=request.user.profile)
    rent_items=models.RentItemsCart.objects.filter(owner=request.user.profile)
    cart_total=0
    for item in cart_items:
        cart_total+=item.amount
    for item in rent_items:
        cart_total+=item.amount
    context={
        "cart_items":cart_items,
        "total":cart_total,
        "rent_items":rent_items
    }
    return render(request,"orders/cart.html",context)
@login_required
def DeleteFromCart(request,item_id):
    item_to_delete = models.CartItems.objects.filter(pk=item_id).delete()
    return show_cart(request)

@login_required
def checkout(request):
    cart_items=list(models.CartItems.objects.filter(owner=request.user.profile))
    rent_items=list(models.RentItemsCart.objects.filter(owner=request.user.profile))
    if cart_items:
        order_cart_total=0
        for item in cart_items:
            order_cart_total+=item.amount
        order,status=models.Order.objects.get_or_create(owner=request.user.profile,total=order_cart_total,order_ref_code=''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]))
        for item in cart_items:
            order_item,status=models.OrderItems.objects.get_or_create(game=item.game,ref_code=item.ref_code,amount=item.amount,order=order)
            if status:   
                item_to_delete = models.CartItems.objects.filter(ref_code=item.ref_code).delete()
            else:
                item.is_ordered=True
    if rent_items:
        rent_cart_total=0
        for item in rent_items:
            rent_cart_total+=item.amount
        rentOrder,status=models.RentOrder.objects.get_or_create(owner=request.user.profile,total=rent_cart_total,order_ref_code=''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]))
        for item in rent_items:
            days=item.duration*7
            due_date=rentOrder.date+timedelta(days=days)
            rent_order_item,status=models.RentItems.objects.get_or_create(game=item.offer.game,ref_code=item.ref_code,amount=item.amount,rentorder=rentOrder,due_date=due_date)
            if status:   
                item_to_delete = models.RentItemsCart.objects.filter(ref_code=item.ref_code).delete()
            else:
                item.is_ordered=True
    return HttpResponseRedirect('/home')

@login_required
def show_orders(request):
    orders=models.Order.objects.filter(owner=request.user.profile)
    context={
        'orders':orders
    }
    return render(request,"orders/show_orders.html",context)

@login_required
def show_order(request,order_id):
    order=models.Order.objects.filter(owner=request.user.profile,pk=order_id)
    order_items=models.OrderItems.objects.filter(order=order[0])
    context={
        'order_items':order_items
    }
    return render(request,"orders/show_order.html",context)
@login_required
def AddToRentCart(request,offer_id):
    user_profile = request.user.profile
    offer = Offers.objects.get(pk=offer_id)
    rent_item_cart,status= models.RentItemsCart.objects.get_or_create(offer=offer,amount=offer.rent,ref_code=''.join([random.choice(string.ascii_letters + string.digits) for n in range(3)]),owner=user_profile,duration=offer.time_period)
    if status:
        rent_item_cart.save()
    return HttpResponseRedirect('/home')

@login_required
def DelFromRentCart(request,offer_id):
    item_to_delete = models.RentItemsCart.objects.filter(pk=offer_id).delete()
    return show_cart(request)

@login_required
def show_rent_orders(request):
    orders=models.RentOrder.objects.filter(owner=request.user.profile)
    context={
        'orders':orders
    }
    return render(request,"orders/show_rent_orders.html",context)

@login_required
def show_rent_order(request,order_id):
    order=models.RentOrder.objects.filter(owner=request.user.profile,pk=order_id)
    order_items=models.RentItems.objects.filter(rentorder=order[0])
    context={
        'order_items':order_items
    }
    return render(request,"orders/show_rent_order.html",context)

@login_required
def show_currently_rented_orders(request):
    orders=list(models.RentOrder.objects.filter(owner=request.user.profile))
    rented_order=[]
    due_orders=[]
    for i in range(len(orders)):
        order_items=list(models.RentItems.objects.filter(rentorder=orders[i]))
        for item in order_items:
            if item.due_date>=date.today():
                rented_order.append(item)
            elif item.due_date<date.today():
                due_orders.append(item)
    context={
        'orders':rented_order,
        'due_orders':due_orders
    }
    return render(request,"orders/show_current_rent_orders.html",context)