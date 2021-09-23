from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

def programming_blog(request):
    blogs=Blog.objects.filter(blog_category="advance programming")
    params={"blog":blogs}

    return render(request, 'blog/programming-blog.html',params)

def view_programming_blog(request,blog_url):
    blogs = Blog.objects.filter(blog_url=blog_url)
    params = {"blog": blogs}
    return render(request, 'blog/view-programming-blog.html',params)

# Create your views here.
