from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, PostView, Like, Comment
from posts.forms import PostForm

# Create your views here.

# vista ListView mustra todos los contenidos del modelo
class PostLisView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post


# Actualizar
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/' # redireccionar a la misma vista en la que se invoca
