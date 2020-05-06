from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def index(request):
    data = dict()
    data['user'] = 'temp_admin'         # Временный пользователь (до вкл.авторизации)
    data['title'] = 'Лента новостей'
    data['posts'] = Post.objects.all()
    return render(request, 'news/index.html', context=data)


def create(request):
    data = dict()
    data['title'] = 'Добавление новости'
    if request.method == 'GET':
        data['form'] = PostForm()
        return render(request, 'news/create.html', context=data)
    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        # перенаправляем на страничку news, а там она добовляется в таблиуц со всеми новостями
        return redirect('/news')


def details(request):
    data = {'title': 'Просмотр новости'}
    return render(request, 'news/details.html', context=data)


def edit(request):
    data = {'title': 'Редактирование новости'}
    return render(request, 'news/edit.html', context=data)


def delete(request):
    data = {'title': 'Удаление новости'}
    return render(request, 'news/delete.html', context=data)


