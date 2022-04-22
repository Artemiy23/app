from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('men', views.men, name='men'),
    path('men/<slug:category_slug>/', views.men, name='men_product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('women', views.women, name='women'),
    path('women/<slug:category_slug>/', views.women, name='women_product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('boys', views.boys, name='boys'),
    path('boys/<slug:category_slug>/', views.boys, name='boys_product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('girls', views.girls, name='girls'),
    path('girls/<slug:category_slug>/', views.girls, name='girls_product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]

