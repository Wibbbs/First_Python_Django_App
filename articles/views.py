from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def list_articles(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})