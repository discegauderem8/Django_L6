from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render('accounts/index.html')  # Замените 'home' на вашу домашнюю страницу
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/registration/login.html')

def logout_view(request):
    logout(request)
    context = {"message": "Вы вышли из аккаунта"}
    return render(request, 'accounts/index.html', context=context)  # Замените 'home' на вашу домашнюю страницу

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # После успешной регистрации перенаправляем пользователя на другую страницу, например, на главную страницу.
            return redirect('mainpage', permanent=True)  # 'index' - это имя URL-шаблона для главной страницы
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



