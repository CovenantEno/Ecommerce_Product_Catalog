from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),
    
    # Categories
    path('categories/', views.category_list_view, name='category_list'),
    path('categories/add/', views.category_create_view, name='category_create'),
    path('categories/<slug:slug>/edit/', views.category_update_view, name='category_update'),
    path('categories/<slug:slug>/delete/', views.category_delete_view, name='category_delete'),

    # Products
    path('products/', views.product_list_view, name='product_list'),
    path('products/add/', views.product_create_view, name='product_create'),
    path('products/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('products/<slug:slug>/edit/', views.product_update_view, name='product_update'),
    path('products/<slug:slug>/delete/', views.product_delete_view, name='product_delete'),
]
