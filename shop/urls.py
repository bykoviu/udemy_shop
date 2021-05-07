from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('goods_and_services/', views.goods_and_services, name="goods_and_services"),
    path('cont/', views.cont, name="cont"),
    path('articles/', views.articles, name="articles"),
    path('product/', views.prod, name='product')
]