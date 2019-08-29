from django.urls import path
from user import views

urlpatterns=[
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('signup',views.signup,name='signup'),
    path('profile/<int:id>',views.profile_view,name='profile'),
    path('profile_update',views.update_profile,name="profile_update")
]