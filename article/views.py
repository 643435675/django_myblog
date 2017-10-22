from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from article.models import Article
from datetime import datetime


# def home(request):
#     return HttpResponse('Hello Django my God')

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,id):
    post_list = Article.objects.all()
    # str_post = ("title = %s,category = %s,date_time = %s,content = %s"
    #         % (post.title,post.category,post.date_time,post.content))
    str_post = ("title = %s, category = %s, date_time = %s, content = %s"
           %(post_list.title, post_list.category, post_list.date_time, post_list.content))
    return HttpResponse(str_post)


def test(request):
    return render(request,'test.html', {'current_time':datetime.now})