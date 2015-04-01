# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from blog.models import Blog
from blog.models import Myself
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.syndication.views import Feed


# Create your views here.

#def home(request):
#    return HttpResponse('Hello World')



def index(request):
    return render_to_response('index.html')

def home(request):
    posts = Blog.objects.all()

    paginator = Paginator(posts,4) #一页显示4篇文章
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request,'home.html',{'post_list':post_list})

def about(request):
    post = Myself.objects.get(id=1)
    return render(request,'about.html',{'post':post})

def post(request,id):
    try:
        post = Blog.objects.get(id = str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def links(request):
    return render_to_response('links.html')

def archive(request):
    try:
        post_list = Blog.objects.all()
    except Blog.DoesNotExist:
        raise Http404
    return render(request,'archive.html',{'post_list':post_list})

class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "/feed"
    description = "RSS feed - blog posts"

    def items(self):
        return Blog.objects.order_by('-time')
    def item_title(self, item):
        return item.title
    def item_pubdate(self,item):
        return item.time
    def item_description(self, item):
        return item.content


