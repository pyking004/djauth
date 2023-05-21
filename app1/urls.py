from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('',views.app1,name='app1'),
    path('signup',views.sign_up,name='signup'),
]
