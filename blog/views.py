from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class PostList(TemplateView):
    model = Post
    template_name = 'index.html'


def index(request):
    return render(request, 'home.html', {})


class TemplateView(ListView):
    model = Post
    template_name = 'index_home.html'


class PostDetail(DeleteView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'author', 'body', 'time']


class PostEdit(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'time']


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index_home')
