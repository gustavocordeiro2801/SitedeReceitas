from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# LISTAGEM - ListView
class ListaPostsView(ListView):
    model = Post
    template_name = 'blog/lista.html'
    context_object_name = 'posts'
    ordering = ['-data_postagem']

# DETALHE - DetailView (retorna 404 automaticamente se não existir)
class DetalhePostView(DetailView):
    model = Post
    template_name = 'blog/detalhe.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

# CRIAR - CreateView
class CriarPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/criar.html'
    success_url = reverse_lazy('lista_posts')

# EDITAR - UpdateView
class EditarPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/editar.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse_lazy('detalhe_post', kwargs={'id': self.object.id})

# EXCLUIR - DeleteView (com página de confirmação)
class ExcluirPostView(DeleteView):
    model = Post
    template_name = 'blog/excluir_confirmar.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_posts')
