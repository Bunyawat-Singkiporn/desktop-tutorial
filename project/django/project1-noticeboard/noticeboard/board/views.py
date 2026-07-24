from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model               = Post
    template_name       = 'board/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model         = Post
    template_name = 'board/post_detail.html'


class PostCreateView(CreateView):
    model         = Post
    form_class    = PostForm
    template_name = 'board/post_form.html'
    success_url   = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = 'board/post_form.html'
    success_url   = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model         = Post
    template_name = 'board/post_confirm_delete.html'
    success_url   = reverse_lazy('post_list')
