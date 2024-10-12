from django.shortcuts import render
from models import news
# Create your views here.

def index(request):
    news=news.objects.all()
    return render(request, 'index.html', {"news":news})
