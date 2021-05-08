from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slud)
        products = Product.objects.filter(category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)

    return render(request, 'base.html', {'category':category_page, 'products':products})


def about(request):
    return render(request, 'about.html')


def goods_and_services(request):
    return render(request, 'goods_and_services.html')


def cont(request):
    return render(request, 'cont.html')


def articles(request):
    return render(request, 'articles.html')

def prod(request):
    return render(request, 'prod.html')

# Create your views here.
