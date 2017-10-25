from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def home(request):
#     return HttpResponse('Hello Django my God')

def home(request):
    post_list = Article.objects.all()
    paginator = Paginator(post_list, 2)  # 每页显示两个
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})

def detail(request,id):
    try:
        post_list = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404

    return render(request,'post.html',{'post':post_list})


def test(request):
    return render(request,'test.html', {'current_time':datetime.now})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list':post_list,'error':False})

def search_tag(request,tag):
    try:
        post_list = Article.objects.fiter(category__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})

def about_me(request):
    return render(request,'aboutme.html')

def blog_search(request):
    if 's' in request.GET:
        string = request.GET['s']
        if not string:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=string)
            if len(post_list) == 0:
                return render(request,'archives.html',{'post_list':post_list,'error':True})
            else:
                return render(request,'archives.html',{'post_list':post_list,'error':False})

    return redirect('/')