from django.shortcuts import render, redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.

def articles_list(request):
    articles = Articles.objects.all().order_by('title')
    return render(request, 'articles/articles_list.html', {'articles': articles})  # Called  'articles_list.html'


def articles_detailes(request, article_name):
    # return HttpResponse(article_name)
    articles = Articles.objects.get(slug=article_name)
    return render(request, 'articles/article_detail.html', {'article': articles})


@login_required(login_url="/accounts/login/")
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES) # "request.FILES" for picture in thumbnail
        if form.is_valid:
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form': form})
