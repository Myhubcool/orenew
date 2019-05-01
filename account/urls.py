from django.urls import path
from . import views

urlpatterns = [
    path('', views.homee, name='homee'),
    path('login/',views.login,name='login'),
    path('loginreq/',views.loginreq,name='loginreq'),
    path('customer_signin/',views.customer_signin,name='customer_signin'),
    path('logout/',views.logout,name='logout'),
    path('verify/',views.verify,name='verify'),
    path('retailer_signin/',views.retailer_signin,name='retailer_signin'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('machanicprofile/',views.machanicprofile,name='machanicprofile'),
    path('filled/', views.filled, name='filled'),
    path('congratulation/', views.congratulation, name='congratulation'),
    path('loggedin/', views.home, name='home'),
    path('mnframe/', views.mnframe, name='mnframe'),
    path('tservice', views.tservice, name='tservice')
    ]
