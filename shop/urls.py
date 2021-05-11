from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('about/', views.about, name='about'),
    path('goods_and_services/', views.goods_and_services, name="goods_and_services"),
    path('cont/', views.cont, name="cont"),
    path('articles/', views.articles, name="articles"),
    path('category/<slug:category_slug>/<slug:product_slug>', views.prod, name='product_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
]