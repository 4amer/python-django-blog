from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article

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
    
