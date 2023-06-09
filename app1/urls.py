from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('',views.app1,name='app1'),
    path('signup',views.sign_up,name='signup'),
    path('login',views.userlogin,name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.userlogout,name='logout'),
    path('changepwd1',views.changepwd1,name='changepwd1'),
    path('changepwd2',views.changepwd2,name='changepwd2'),
    path('userinfo/<int:id>',views.userinfo,name='userinfo'),
]

