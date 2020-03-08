from django.shortcuts import render

# Create your views here.
def list_articles(request):
    return render(request, 'articles/articles.html')