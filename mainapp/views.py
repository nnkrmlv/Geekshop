from django.shortcuts import render
from datetime import date
from mainapp.models import Product, ProductCategory, Menu
# Create your views here.
# контроллер = функция - view
# MVC - Model View Controller
# MVT - Model View Template


def index(request):
    context = {
        'title': 'GeekShop',
        # 'authorized': False,
        # 'user': 'Инна К.',
        'today': date.today()
              }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):

    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'title': 'GeekShop - Каталог',
        # 'authorized': True,
        # 'user': 'Инна К.',
        'basket': {'to_basket': 'Отправить в корзину', 'out_of_basket': 'Удалить из корзины'},
        'menu': Menu.objects.all(),
               }

    #           }
    return render(request, 'mainapp/products.html', context)
