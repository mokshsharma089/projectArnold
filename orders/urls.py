from django.urls import path
from orders import views

urlpatterns=[
    path('add_to_cart/<int:game_id>',views.AddToCart,name='AddToCart'),
    path('show_cart',views.show_cart,name="show_cart"),
    path('delete_from_cart/<int:item_id>',views.DeleteFromCart,name='DeleteFromCart'),
    path('checkout',views.checkout,name="checkout"),
    path('show_orders',views.show_orders,name='show_orders'),
    path('show_order/<int:order_id>',views.show_order,name='show_order'),
    path('AddToRentCart/<int:offer_id>',views.AddToRentCart,name="AddToRentCart"),
    path('delFromRentCart/<int:offer_id>',views.DelFromRentCart,name="DelFromRentCart"),
    path('show_rent_orders',views.show_rent_orders,name="show_rent_orders"),
    path('show_rent_order/<int:order_id>',views.show_rent_order,name="show_rent_order"),
    path('show_currently_rented_orders',views.show_currently_rented_orders,name='show_currently_rented_orders')
]