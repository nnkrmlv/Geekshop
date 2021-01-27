from django.shortcuts import render
from datetime import date

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


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'authorized': False,
        'user': 'Инна К.',

              }
    return render(request, 'mainapp/products.html', context)
