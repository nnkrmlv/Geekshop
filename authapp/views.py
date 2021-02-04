from django.shortcuts import render
from authapp.forms import UserLoginForm
from authapp.models import User
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(date=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HTTPResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    contex = {'form': form}

    return render(request, 'authapp/login.html')


def register(request):
    return render(request, 'authapp/register.html')
