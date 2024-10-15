from django.shortcuts import render
from models import news
# Create your views here.

def index(request):
    news=news.objects.all()
    return render(request, 'index.html', {"news":news})

from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})

def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article_list')
