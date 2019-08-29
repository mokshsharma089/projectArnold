from django.urls import path
from home import views

urlpatterns=[
    path('',views.index,name='pArnold'),
    path('home',views.home,name='home'),
    path('game/<int:id>',views.game_page,name='get_game')
]