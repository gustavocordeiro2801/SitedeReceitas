from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()
        return context

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

# CRIAR COMENTÁRIO - Função
@login_required
def criar_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('detalhe_post', id=post.id)
    else:
        form = CommentForm()
    
    return render(request, 'blog/criar_comentario.html', {'form': form, 'post': post})
