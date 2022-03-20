from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView
)
from .models import Post

#from django.http import HttpResponse

#posts = [
   # {
   #     'author' : 'Kamila',
    #    'title' : 'Blog post 1',
     #   'content' : 'First post content',
      #  'date_posted' : 'August 27, 2018'
   # },
   # {
    #    'author' : 'Jesio',
     #   'title' : 'Blog post 2',
      #  'content' : 'second post content',
       # 'date_posted' : 'August 28, 2018'
  #  }
#]


def home(request):
    context = {
        'posts': Post.objects.all() 
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    
    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
# Create your views here.
