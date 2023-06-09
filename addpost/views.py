from django.shortcuts import render
from django.views import View
from .models import Blog
# Create your views here.
from .forms import BlogForm

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-created_on')
        form = BlogForm()
        context = {
            'blog_list' : blogs,
            'form' :form,
            'name': request.user
        }

        return render(request, 'addpost/blog.html', context)
    def post(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-created_on')
        form = BlogForm(request.POST)

        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()

        context = {
            'blog_list' : blogs,
            'form' :form,
            'name' : request.user
        }

        return render(request, 'addpost/blog.html', context)
        
  
class BlogView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-created_on')
        form = BlogForm()
        context = {
            'blog_list' : blogs,
            'form' :form,
            'name': request.user
        }
        return render(request, 'addpost/blogindex.html', context)
    def post(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-created_on')
        form = BlogForm()
        context = {
            'blog_list' : blogs,
            'form' :form,
            'name': request.user
        }
        return render(request, 'addpost/blogindex.html', context)
        
