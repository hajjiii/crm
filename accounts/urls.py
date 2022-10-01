from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('products/', views.products,name='products'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('customer/<str:pk_test>/', views.customer,name='customer'),

]
