from django.shortcuts import render

from new_app.models import news
# Create your views here.

def index(request):
    news.objects.all()
    return render(request, 'index.html', {"news":news})

def other_page(request):
    return render(request, 'other_page.html', {"news":news})

