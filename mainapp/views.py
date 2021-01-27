from django.shortcuts import render

# Create your views here.
# контроллер = функция - view
# MVC - Model View Controller
# MVT - Model View Template


def index(request):
    context = {
        'title': 'GeekShop',
        'authorized': True,
        'user': 'Инна К.',
              }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'authorized': True,
        'user': 'Инна К.',

              }
    return render(request, 'mainapp/products.html', context)
