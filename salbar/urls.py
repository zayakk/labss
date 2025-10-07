from django.urls import path
from salbar import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),       
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('store/', views.store, name='store'),
    path('product/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search_result, name='search_result'),
    path('<slug:category_slug>/', views.store, name='store_by_category'),


]
