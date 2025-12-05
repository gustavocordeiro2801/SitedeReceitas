from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# LISTAGEM
def lista_posts(request):
    posts = Post.objects.all().order_by('-data_postagem')
    return render(request, 'blog/lista.html', {'posts': posts})

# DETALHE
def detalhe_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detalhe.html', {'post': post})

# CRIAR POST (com Django Forms)
def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    
    return render(request, 'blog/criar.html', {'form': form})

# EDITAR POST (com Django Forms)
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalhe_post', id=post.id)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/editar.html', {'form': form, 'post': post})

# EXCLUIR POST (com confirmação)
def excluir_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')

    return render(request, 'blog/excluir_confirmar.html', {'post': post})
