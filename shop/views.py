from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


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
