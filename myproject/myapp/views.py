from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


def page1(request):
    return HttpResponse("<h1>Головна сторінка</h1><a href='/page2/'>Перейти на інформаційну сторінку    </a>")


def page2(request):
    return HttpResponse("<h1>Інформаційна сторінка</h1><a href='/page1/'>Перейти на головну сторінку</a>")


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'myapp/article_list.html', {'articles': articles})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'myapp/article_form.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'myapp/article_confirm_delete.html', {'article': article})

