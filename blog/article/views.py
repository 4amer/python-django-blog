from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout

from django.contrib import messages

from .models import Article
from .forms import CreateUserForm

from django.utils import timezone

def index(request):
    article = Article.objects.all()
    return render(request, 'article/list.html', {'article': article})

def pub_article(request):
    a = Article(article_text = request.POST['name'], 
        article_content = request.POST['content'],
        article_date = timezone.now())
    a.save()
    return HttpResponseRedirect ( reverse('article:index'))
    
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Аккаунт под именем " + user + ", был создан!")
            return redirect('article:login')


    context = {'form': form }
    return render (request, 'article/register.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('article:index')
        else:
            messages.info(request, "Пользователь ИЛИ пароль не верны!")

    context = {}
    return render (request, 'article/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('article:login')

