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
        'authorized': False,
        'user': 'Инна К.',
        'today': date.today()
              }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):

    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'title': 'GeekShop - Каталог',
        'authorized': True,
        'user': 'Инна К.',
        'basket': {'to_basket': 'Отправить в корзину', 'out_of_basket': 'Удалить из корзины'},
        'menu': Menu.objects.all(),
               }
    # context = {
    #
    #     'products': [
    #         {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб', 'details': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'in_basket': False, 'img': 'vendor/img/products/Adidas-hoodie.png'},
    #         {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб', 'details': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'in_basket': True, 'img': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
    #         {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.', 'details': 'Материал с плюшевой текстурой. Удобный и мягкий', 'in_basket': False, 'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
    #         {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.', 'details': 'Плотная ткань. Легкий материал.', 'in_basket': False, 'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
    #         {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.', 'details': 'Гладкий кожаный верх. Натуральный материал', 'in_basket': False, 'img': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
    #         {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.', 'details': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'in_basket': False, 'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
    #     ],
    #           }
    return render(request, 'mainapp/products.html', context)
